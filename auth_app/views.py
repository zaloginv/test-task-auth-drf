
from django.http import HttpRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CheckUserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request: HttpRequest):
        return Response()