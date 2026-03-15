FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt && apt-get install -y ca-certificates

EXPOSE 5000

CMD ["python","app/app.py"]