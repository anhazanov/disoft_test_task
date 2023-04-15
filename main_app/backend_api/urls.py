from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import TasksViewSet, TasksStatusViewSet, TasksImagesViewSet, CommentsViewSet

router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasks')
router.register(r'tasksstatus', TasksStatusViewSet, basename='tasksstatus')
router.register(r'tasksimages', TasksImagesViewSet, basename='tasksimages')
router.register(r'comments', CommentsViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls))
]
