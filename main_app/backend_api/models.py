from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class TasksStatus(models.Model):
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.status


class Tasks(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    status = models.ForeignKey(TasksStatus, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    performers = models.ManyToManyField(User, blank=True, related_name='performers')
    date_create = models.DateField(default=now)
    date_update = models.DateField(blank=True, null=True)


class TasksImages(models.Model):
    image = models.ImageField(upload_to='media/')
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.CharField(max_length=255, blank=True)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    comment_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
