from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from api.account.models import User

class CreateUserSerializer(ModelSerializer):

    password=serializers.CharField(required=True,min_length=8)
    
    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True,'read_only': False}}
        fields = ["email","password"]


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        "no_active_account": {"message":"Bad Request No active account found with the given credentials"}
    }
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'],token['user_role'] = user.email,user.user_role
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        return data