FROM python:3.10.6-slim-buster AS base

WORKDIR /app
COPY . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]