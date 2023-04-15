from django.core.mail import send_mail


def send(user_email: str):
    send_mail(
        subject='You are have a new task.',
        message='Faster go work!',
        from_email='djangobackend86@gmail.com',
        recipient_list=[user_email],
        fail_silently=False,
    )