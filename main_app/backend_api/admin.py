from django.contrib import admin

from .models import TasksStatus, Tasks, TasksImages, Comments

admin.site.register(TasksStatus)
admin.site.register(Tasks)
admin.site.register(TasksImages)
admin.site.register(Comments)
