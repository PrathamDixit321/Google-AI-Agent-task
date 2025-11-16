# Run Uvicorn server for AI-PGOS
$env:PYTHONPATH = "$PWD\src;$env:PYTHONPATH"
python -m uvicorn src.app:app --host 127.0.0.1 --port 8000
