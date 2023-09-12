from django.core.mail import send_mail
from django.conf import settings

def sendmail():
    subject="testing"
    message="this is testing message"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["aaryanshah615@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)
    