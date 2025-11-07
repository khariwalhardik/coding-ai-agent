Calculator micro-app

This is a tiny Flask-based calculator used for local testing and demonstration.

How to run (PowerShell on Windows):

1. Create and activate a virtual environment (optional but recommended):

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Install dependencies (from top-level `requirements.txt` or install Flask):

   pip install -r ..\requirements.txt

3. Run the app:

   python -m calculator.app

Open http://127.0.0.1:5000 in your browser.
