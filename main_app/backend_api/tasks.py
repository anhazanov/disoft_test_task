from main_app.celery import app
from .services import send


@app.task
def send_mail(email_list):
   for email in email_list:
      send(email)
