# AI Document Scanner + Summarizer

**Short description**

A Python project that extracts text from PDFs using Azure Document Intelligence (Form Recognizer) and summarizes the extracted text using Groq LLMs. Built as a lightweight pipeline you can run locally or deploy later as a web app.

---

## Features

* Batch-processing of PDF files in a folder
* Text extraction using Azure Document Intelligence (prebuilt `layout`)
* Summarization using Groq `llama-3.1-8b-instant` (chat completion)
* Saves or prints summaries per file
* `.env` support for storing API keys
* Simple formatting for recruiter-friendly presentation

---

## Tech stack / Tools / Libraries / APIs used

* **Python 3.8+**
* **Azure Document Intelligence** (Form Recognizer) — `azure-ai-formrecognizer`
* **Azure core** — `azure-core`
* **Groq API / Groq Python SDK** — `groq`
* **python-dotenv** for loading environment variables (`.env`)

Other helpful tools while developing:

* VS Code / Anaconda (development environment)
* Git & GitHub for version control and portfolio
* Postman or curl for quick API tests

---

## Setup (local)

1. Clone the repo

```bash
git clone https://github.com/<your-username>/AI-Document-Summarizer.git
cd AI-Document-Summarizer
```

2. Create and activate a virtual environment (or use conda)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root (DO NOT commit this file). Add your keys:

```
AZURE_KEY=<your_azure_form_recognizer_key>
GROQ_KEY=<your_groq_api_key>
AZURE_ENDPOINT=https://<your-resource-name>.cognitiveservices.azure.com/
```

5. Run the script

```bash
python AI_Scanner_Summ.py
```

*** IMPORTANT ***
```
Make sure that you change the filepath to yours
```

---

## Screenshots 
Below are the screenshots I took of my output(terminal) after running the code.

Extracted text #1
<img width="1462" height="148" alt="Screenshot 2025-12-05 234717" src="https://github.com/user-attachments/assets/9a81ff48-9296-4075-ad4e-01800d1778ee" />

Summarised text #1
<img width="1454" height="205" alt="Screenshot 2025-12-05 234733" src="https://github.com/user-attachments/assets/772a3195-d791-4d79-a16a-5774dd7679c8" />

Extracted text #2
<img width="1465" height="280" alt="Screenshot 2025-12-05 234746" src="https://github.com/user-attachments/assets/94894c98-485f-454e-882d-466315d310f6" />

Summarised text #2
<img width="1479" height="406" alt="Screenshot 2025-12-05 234758" src="https://github.com/user-attachments/assets/14211f42-3740-4b2a-88d4-42dede64b3e7" />

---
