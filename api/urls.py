from django.urls import path, include
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
from rest_framework.routers import DefaultRouter
from .views import (
        PostViewSet, 
        CommentViewSet, 
        APIFollow, 
        APIGroup,
    ) 



router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>[^/.]+)/comments', CommentViewSet)



urlpatterns = [
        path('', include(router.urls)),
        path('follow/', APIFollow.as_view()),
        path('group/', APIGroup.as_view()),

        path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        
    ]

