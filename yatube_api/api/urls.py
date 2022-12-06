from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('follow', FollowViewSet, basename='followers')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('groups', GroupViewSet)

jwt_patterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view, name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('v1/auth/', include(jwt_patterns)),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
