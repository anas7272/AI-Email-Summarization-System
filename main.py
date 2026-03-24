import os
import pickle
from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import datetime
from openai import OpenAI


load_dotenv()

def get_ai_client():
    openai_key = os.getenv("OPENAI_API_KEY")
    github_token = os.getenv("GITHUB_TOKEN")

    # ✅ Only use OpenAI if key is valid AND non-empty
    if openai_key and openai_key.strip() != "":
        print(" Using OpenAI API")
        return OpenAI(api_key=openai_key)

    elif github_token and github_token.strip() != "":
        print(" Using GitHub Models API")
        return OpenAI(
            api_key=github_token,
            base_url="https://models.inference.ai.azure.com"
        )

    else:
        raise ValueError(" No API key found")


client = get_ai_client()

# Gmail scope
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# File paths
TOKEN_FILE = "token.pickle"
CREDENTIALS_FILE = "credentials.json"


def gmail_service():
    creds = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)


def search_emails(service, query, max_results=50):
    results = service.users().messages().list(
        userId='me',
        q=query,
        maxResults=max_results
    ).execute()

    return results.get('messages', [])


def read_email(service, msg_id):
    message = service.users().messages().get(
        userId='me',
        id=msg_id,
        format='metadata',
        metadataHeaders=['From', 'Subject', 'Date']
    ).execute()

    headers = message['payload']['headers']
    snippet = message.get('snippet')

    email_data = {'From': '', 'Subject': '', 'Date': '', 'Snippet': snippet}

    for header in headers:
        if header['name'] == 'From':
            email_data['From'] = header['value']
        elif header['name'] == 'Subject':
            email_data['Subject'] = header['value']
        elif header['name'] == 'Date':
            email_data['Date'] = header['value']

    return email_data


def ai_summarize_email(subject, snippet):
    prompt = f"""
    Summarize this email in ONE short line.
    Focus on main purpose or topic.

    Subject: {subject}
    Content: {snippet}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You summarize emails clearly."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=30,
            temperature=0.3
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("⚠️ AI failed:", e)
        return "Summary unavailable"


if __name__ == "__main__":
    print("📧 Gmail Search Tool (type 'exit' to quit)\n")

    service = gmail_service()

    while True:
        user_input = input(
            "Enter query and count (example: subject:otp,10): "
        ).strip()

        if user_input.lower() == "exit":
            print("Exiting Gmail tool 👋")
            break

        if "," in user_input:
            query_part, count_part = user_input.split(",", 1)
            query = query_part.strip()
            max_results = int(count_part.strip()) if count_part.strip().isdigit() else 50
        else:
            query = user_input
            max_results = 50

        messages = search_emails(service, query, max_results)

        print(f"\nFound {len(messages)} messages\n")

        for msg in messages:
            email = read_email(service, msg['id'])
            summary = ai_summarize_email(email['Subject'], email['Snippet'])

            print("From:", email['From'])
            print("Subject:", email['Subject'])
            print("Date:", email['Date'])
            print("AI Summary:", summary)
            print("-" * 50)