from pathlib import Path
from flask import Flask, send_from_directory

BASE_DIR = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)

@app.get("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")

@app.get("/health")
def health():
    return {"status": "ok", "application": "phishlab-awareness-demo"}

if __name__ == "__main__":
    # Local development only. Render runs the app with Gunicorn.
    app.run(host="127.0.0.1", port=5000, debug=False)
