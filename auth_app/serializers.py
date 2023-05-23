from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        jwt = get_tokens_for_user(user)
        user.access = jwt["access"]
        user.refresh = jwt["refresh"]
        user.save()
        return user
