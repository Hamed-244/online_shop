FROM python:3.13.0a1
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080
CMD bash -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"