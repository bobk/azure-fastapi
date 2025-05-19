set PYTHONDONTWRITEBYTECODE=1
start uvicorn app.main:app --reload --host 0.0.0.0 --port 5000 --log-level debug
