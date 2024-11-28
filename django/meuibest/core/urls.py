from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CreatorViewSet, CategoryViewSet, ChannelViewSet, UserViewSet, GroupViewSet

router = DefaultRouter()
router.register(r'creators', CreatorViewSet, basename='creator')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'channels', ChannelViewSet, basename='channel')
router.register(r'users', UserViewSet, basename='user')
router.register(r'group', GroupViewSet, basename='group')

urlpatterns = [
  
]