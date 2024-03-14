FROM python:3.13-rc-slim-bookworm
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8080
CMD ["gunicorn","--config", "wsgi.py", "app:app"]