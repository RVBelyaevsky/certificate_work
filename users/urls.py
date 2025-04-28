from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from django.urls import path

from users.views import (
    UserCreateAPIView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
    UserDestroyAPIView,
    UserListAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("", UserListAPIView.as_view(), name="users_list"),
    path("create/", UserCreateAPIView.as_view(), name="user_create"),
    path("update/<int:pk>/", UserUpdateAPIView.as_view(), name="user_update"),
    path("retrieve/<int:pk>/", UserRetrieveAPIView.as_view(), name="user_retrieve"),
    path("destroy/<int:pk>/", UserDestroyAPIView.as_view(), name="user_destroy"),
]
