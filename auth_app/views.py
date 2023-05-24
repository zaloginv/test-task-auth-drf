from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = User.objects.get(username=serializer.data["username"])
        jwt = get_tokens_for_user(user)
        return Response(jwt)

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = "http://127.0.0.1:8000/api/auth/google/callback/"

class CheckUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: HttpRequest):
        return Response({"hello":"hi"})

