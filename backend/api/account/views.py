import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from django.db import IntegrityError

from api.account.models import User
from api.account.serializers import CreateUserSerializer,MyTokenObtainPairSerializer

logger = logging.getLogger(__name__)

class CreateUserView(APIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = User.objects.create(email=serializer.data['email'])
                user.set_password(serializer.data['password'])
                user.save()
                return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
        except IntegrityError as Interror :
            logger.info(Interror)
            return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
        except Exception as e :
            logger.info(e)
            return Response({"message":"Something Went Wrong"},status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
