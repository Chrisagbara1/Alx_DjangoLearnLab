from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, feed

from django.urls import path, include
from .views import like_post, unlike_post

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', feed, name='feed'),
    
    path("<int:pk>/like/", like_post, name="like-post"),
    path("<int:pk>/unlike/", unlike_post, name="unlike-post"),
]