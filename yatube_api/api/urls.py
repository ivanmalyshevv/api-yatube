from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.authtoken import views as drf_views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='group')

comments_list = CommentViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
comments_detail = CommentViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

urlpatterns = [
    path(
        'api-token-auth/',
        drf_views.obtain_auth_token,
        name='api_token_auth'
    ),
    path('', include(router.urls)),
    path('posts/<int:post_id>/comments/', comments_list, name='comments-list'),
    path(
        'posts/<int:post_id>/comments/<int:pk>/',
        comments_detail,
        name='comments-detail'
    ),
]
