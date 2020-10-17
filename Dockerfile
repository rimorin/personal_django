FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /django_code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

