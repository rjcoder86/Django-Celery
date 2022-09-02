import os
from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_email():
    email = EmailMessage(
        subject='Test Mail',  #mail subject
        body="Testing Celery for sending mail",  #mail body
        from_email=os.environ.get('EMAIL_HOST_USER'), #sender email
        to=('rohit.jadhav@weagile.net',) #tuple of reciever's email ids
    )
    email.send()
    return {'msg':'Done'}