from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from auth_app.views import RegisterView, CheckUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('check/', CheckUserView.as_view(), name='check'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]