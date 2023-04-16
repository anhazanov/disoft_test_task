from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from django.urls import path, include
from django.views.generic import TemplateView

from .views import TasksViewSet, TasksStatusViewSet, TasksImagesViewSet, CommentsViewSet

router = DefaultRouter()
router.register(r'tasks', TasksViewSet, basename='tasks')
router.register(r'tasksstatus', TasksStatusViewSet, basename='tasksstatus')
router.register(r'tasksimages', TasksImagesViewSet, basename='tasksimages')
router.register(r'comments', CommentsViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('api_schema', get_schema_view(
        title='API Schema',
        description='Guide for the REST API'
    ), name='api_schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),
]
