FROM python:3.13-rc-slim-bookworm
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN python manage.py makemigrations && python manage.py migrate
EXPOSE 8080
CMD ["gunicorn", "configs.wsgi", "-b", "0.0.0.0:8080"]