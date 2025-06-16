from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

class UserProfileSeriaizer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password'
        )

class UserRefreshAPISeriaizer(serializers.ModelSerializer):

    access = serializers.CharField()

    class Meta:
        model = User
        fields = (
            'access',
        )

class UserApiDocProfileSeriaizer(serializers.ModelSerializer):

    refresh = serializers.CharField()
    access = serializers.CharField()


    class Meta:
        model = User
        fields = (
            'refresh',
            'access',
            'id',
            'username',
            'password'
        )

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user_serializer = UserProfileSeriaizer(self.user)
        data.update(user_serializer.data)
        return data