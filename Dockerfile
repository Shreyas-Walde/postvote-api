FROM python:3.13.5

WORKDIR /usr/src/app

COPY requirements-backup.txt ./

RUN pip install --no-cache-dir -r requirements-backup.txt

COPY . . 

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

