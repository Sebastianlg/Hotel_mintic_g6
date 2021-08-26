from django.conf import settings
from rest_framework import status
from rest_framework.response import Response 
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.views import APIView
from .models import hotelUser

class VerifyTokenView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            valid_data = tokenBackend.decode(token, verify=False)
            serializer.validated_data['UserId'] = valid_data['user_id']

        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class registroView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        print(data)

        if(len(data['username']) > 3 and len(data['password']) > 4):
            user = hotelUser.objects.create_user(data['username'], data['password'])
            user.save()
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            error = {
                'message': 'Datos invalidos'
            }
            return Response(error, status=status.HTTP_400_BAD_REQUEST)