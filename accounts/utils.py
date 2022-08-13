from email import message
from email.message import EmailMessage
from django.conf import Settings, settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage
from django.conf import settings
def detectUser(user):
    if user.role == 1:
        redirectUrl = 'vendorDashboard'
    if user.role == 2:
        redirectUrl = 'custDashboard'
    elif user.role == None and user.is_superadmin:
        redirectUrl = '/admin'
    return redirectUrl

def send_verification_email(request,user, mail_subject,path):
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    mail_subject = mail_subject
    message = render_to_string(path,{
        'user': user,
        'domain': current_site,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })
    to_email = user.email
    mail = EmailMessage(mail_subject,message,from_email , to = [to_email])
    mail.send()

def send_notification(mail_subject,mail_template,context):
    from_email = settings.DEFAULT_FROM_EMAIL
    message = render_to_string(mail_template,context)
    to_email = context['user'].email
    mail = EmailMessage(mail_subject,message,from_email,to = [to_email])
    mail.send()