import time

from celery import shared_task
from django.core.mail import send_mail, mail_admins


@shared_task
def create_task(task_type):
    time.sleep(int(task_type) * 10)
    return True

@shared_task
def send_email_task(email, question):
    send_mail(
        "Your question was submitted",
        "Thank you for your message, we will get back to you soon",
        from_email='lieschen.yakov@gmail.com',
        recipient_list=[email,],
        fail_silently=False,
    )
    mail_admins("A new question requires your attention", "A new question from {} . The question is as follows {} " .format(email, question))
    return None