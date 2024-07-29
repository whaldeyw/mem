FROM python:latest

WORKDIR /app

COPY requirements.txt .

COPY create_db.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD  [ "python" , "create_db.py" ]
