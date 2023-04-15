from rest_framework.serializers import ModelSerializer, StringRelatedField, SlugRelatedField, SerializerMethodField

from .models import TasksStatus, Tasks, TasksImages, Comments


class TasksStatusSerializer(ModelSerializer):
    class Meta:
        model = TasksStatus
        fields = '__all__'


class TasksSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')
    performers = SlugRelatedField(many=True, read_only=True, slug_field='username')
    status = StringRelatedField()
    images = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Tasks
        fields = '__all__'

    def get_images(self, obj):
        queryset = TasksImages.objects.filter(task=obj)
        return [str(query.image) for query in queryset]

    def get_comments(self, obj):
        queryset = Comments.objects.filter(task=obj)
        return [str(query.comment) for query in queryset]


class TasksImagesSerializer(ModelSerializer):
    class Meta:
        model = TasksImages
        fields = '__all__'


class CommentsSerializer(ModelSerializer):
    task = SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Comments
        fields = '__all__'
