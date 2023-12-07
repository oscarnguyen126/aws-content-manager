FROM python:3.11

WORKDIR /www
COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "content_manager.wsgi:application"]
