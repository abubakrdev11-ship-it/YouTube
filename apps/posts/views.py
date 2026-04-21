from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Video, Like, Views
from .serializers import VideoSerializer, LikeSerializer, ViewsSerializer

@extend_schema(
    summary="Управление видео",
    description="CRUD операции для видео с возрастными ограничениями",
    examples=[
        OpenApiExample(
            "Пример видео",
            value={
                "title": "Моё видео",
                "description": "Описание видео",
                "age_rating": "G",
                "video_file": "path/to/video.mp4",
                "thumbnail": "path/to/thumbnail.jpg"
            }
        )
    ]
)
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('-created_at')
    serializer_class = VideoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ViewsViewSet(viewsets.ModelViewSet):
    queryset = Views.objects.all()
    serializer_class = ViewsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)