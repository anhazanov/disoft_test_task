from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Tasks
from .tasks import send_mail


@receiver(post_save, sender=Tasks)
def post_save_user(**kwargs):
    if kwargs.get('created'):
        performers = kwargs.get('instance').performers.all()
        email_list = [query.email for query in performers]
        send_mail.delay(email_list)
