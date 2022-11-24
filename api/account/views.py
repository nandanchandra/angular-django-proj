import logging

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from django.db import IntegrityError

from api.account.models import User
from api.account.serializers import CreateUserSerializer,MyTokenObtainPairSerializer
from api.utils.email_utils import Util

from backend.settings import DOMAIN

logger = logging.getLogger(__name__)

class CreateUserView(APIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                user = User.objects.create(email=serializer.data['email'])
                user.set_password(serializer.data['password'])
                user.save()
                try:
                    email_body = 'Hello '+user.email+'<br><br>Thank you for signing up on Angular Django.' + '<br><br>Team,<br>AngularDjango<br>'+'______________________________________________________________________________________________<br>'+'This is an automatically generated email, please do not reply. If you need to contact us, please send us an email at<br>'+'chandranandan.chandrakar@gmail.com<br>'+'<br>Copyright © 2021 implicitdefcncdragneel<br>'+'<br>All rights reserved.'
                    data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Greetings from implicitdefcncdragneel'}
                    Util.send_email(data)
                except Exception as e:
                    logger.error(str(e))
                return Response({"message":"User Created Successfully"},status=status.HTTP_201_CREATED)
        except IntegrityError as Interror :
            logger.info(Interror)
            return Response(serializer.errors,status=status.HTTP_403_FORBIDDEN)
        except Exception as e :
            logger.info(e)
            return Response({"error":"USER_EXITS"},status=status.HTTP_400_BAD_REQUEST)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
