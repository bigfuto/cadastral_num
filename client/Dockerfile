
FROM python:3.10-slim

COPY requirements.txt ./app/

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
