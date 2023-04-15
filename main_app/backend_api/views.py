from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Tasks, TasksStatus, TasksImages, Comments
from .serializers import TasksSerializer, TasksStatusSerializer, TasksImagesSerializer, CommentsSerializer
from .permissions import IsPerformers


class TasksStatusViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = TasksStatus.objects.all()
    serializer_class = TasksStatusSerializer


class TasksViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsPerformers]
    queryset = Tasks.objects.all().select_related('author').select_related('status').prefetch_related('performers')
    serializer_class = TasksSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['title', 'text']
    ordering_fields = ['date_create', 'date_update', 'author', 'status']


class TasksImagesViewSet(ModelViewSet):
    queryset = TasksImages.objects.all()
    serializer_class = TasksImagesSerializer


class CommentsViewSet(ModelViewSet):
    permission_classes = [IsAdminUser, IsPerformers]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
