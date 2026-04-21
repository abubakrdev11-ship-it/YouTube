from rest_framework import serializers
from .models import Video, Like, Views

class VideoSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source='author.username', read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = ['id', 'author', 'author_username', 'title', 'description', 'video_file', 'thumbnail', 'created_at', 'age_rating', 'views_count', 'likes_count', 'is_liked']
        read_only_fields = ['id', 'created_at', 'views_count', 'likes_count', 'author']

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Like.objects.filter(user=request.user, video=obj).exists()
        return False

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'video', 'created_at']
        read_only_fields = ['id', 'created_at', 'user']

class ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Views
        fields = ['id', 'user', 'video', 'timestamp']
        read_only_fields = ['id', 'timestamp', 'user']

