# PhishLab Awareness Demo

A clearly labelled, fictional login-page demonstration for authorized security-awareness training.

## Safety and privacy behavior

- The page is explicitly labelled as a security-awareness simulation.
- It does not read form values in JavaScript.
- It does not submit, transmit, or store usernames or passwords.
- It does not authenticate users.
- The visitor can choose to continue to the official Instagram website using a normal link.
- The Flask app serves the page and exposes a basic health endpoint; it does not collect visitor credentials or identifiers.

## Run locally

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Deploy on Render

1. Push the contents of this folder to a GitHub repository.
2. In Render, choose **New → Web Service** and connect the repository.
3. Use these settings:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
4. Deploy. Render will provide an HTTPS URL.

Do not remove the simulation notice or repurpose this page to collect real credentials.
