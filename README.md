# 📧 AI Email Summarization System

An AI-powered Gmail tool that reads emails and generates **one-line summaries** using either **OpenAI API** or **GitHub Models (GPT-4o-mini)**.

---

## 🚀 Features

* 📥 Fetch emails using Gmail API
* 🧠 AI-generated summaries
* 🔄 Supports **multiple AI providers**:

  * OpenAI
  * GitHub Models
* 🔐 Secure environment-based API handling
* ⚡ Fast and simple CLI interface

---

## 📦 Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

### 2. Create virtual environment (optional but recommended)

```
python -m venv venv
```

Activate it:

**Windows (PowerShell):**

```
.\venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ⚙️ Environment Setup

### 1. Create `.env` file

Copy `.env.example` → `.env`

```
OPENAI_API_KEY=
GITHUB_TOKEN=
```

---

## 🔑 AI API Setup (Choose ONE)

---

### 🔹 Option 1: OpenAI API (Recommended)

#### Steps:

1. Go to: https://platform.openai.com/
2. Login / Sign up
3. Navigate to: https://platform.openai.com/api-keys
4. Click **Create new secret key**
5. Copy the key

#### Add to `.env`:

```
OPENAI_API_KEY=your_openai_key_here
```

---

### 🔹 Option 2: GitHub Models (Free Alternative)

#### Steps:

1. Go to: https://github.com/settings/tokens
2. Click **Generate new token (classic)**
3. Select permissions:

   * ✅ `read:packages`
4. Generate token
5. Copy the token

#### Add to `.env`:

```
GITHUB_TOKEN=your_github_token_here
```

---

### ⚠️ Important Notes

* You only need **ONE API**
* If both are provided → OpenAI will be used by default
* If none are provided → the app will not run

---

## 📧 Gmail API Setup (Required)

### 1. Go to Google Cloud Console

https://console.cloud.google.com/

---

### 2. Create a project

* Click **Select Project → New Project**

---

### 3. Enable Gmail API

* Go to **APIs & Services → Library**
* Search: **Gmail API**
* Click **Enable**

---

### 4. Configure OAuth Consent Screen

* Go to **OAuth consent screen**
* Choose **External**
* Fill basic details (App name, Email)
* Save

---

### 5. Create Credentials

* Go to **Credentials**
* Click **Create Credentials → OAuth Client ID**
* Select:

  * Application type → **Desktop App**

---

### 6. Download credentials

* Download JSON file
* Rename it to:

```
credentials.json
```

* Place it in project root folder

---

## ▶️ Run the Project

```
python main.py
```

---

### First Run

* A browser window will open
* Login with your Gmail
* Allow permissions

👉 This will create:

```
token.pickle
```

---

## 💡 Usage

Example input:

```
subject:otp,5
```

This will:

* Search emails with "otp"
* Return 5 results
* Show AI summaries

---

## 📁 Project Structure

```
project/
│
├── main.py
├── requirements.txt
├── .env.example
├── credentials.json   (user provides)
├── token.pickle       (auto-generated)
```

---

## 🔒 Security Notes

Do NOT upload:

```
.env
credentials.json
token.pickle
```

Add to `.gitignore`:

```
.env
credentials.json
token.pickle
__pycache__/
```

---

## 🧠 Tech Stack

* Python
* Gmail API
* OpenAI API / GitHub Models
* dotenv

---

## 💼 Resume Description

Built an AI-powered Gmail email summarization tool with multi-provider LLM support (OpenAI & GitHub Models), secure environment-based configuration, and real-time email parsing using Gmail API.

---

## 👨‍💻 Author

Your Name

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
