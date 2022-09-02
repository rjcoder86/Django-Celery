from django.http import HttpResponse
from .task import send_email
# Create your views here.

def index(request):
    return HttpResponse ("<a href='sendmail'  %}'>Send Mail</a>")

def sendmail(request):
    send_email.delay()
    return HttpResponse('mail sent')