FROM python:2.7-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.og -r requirements.txt

EXPOSE 8080

ENV NAME World

CMD ["python", "app.py"]