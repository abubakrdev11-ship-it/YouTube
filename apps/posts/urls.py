from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VideoViewSet, LikeViewSet, ViewsViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'views', ViewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
