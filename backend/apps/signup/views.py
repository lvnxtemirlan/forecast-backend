from django.contrib.auth.models import Group
from backend.apps.signup.models import CustomUser, Token
from rest_framework import viewsets
from rest_framework import permissions
from backend.apps.signup.serializers import UserSerializer, GroupSerializer, CustomUserSerializer
from rest_framework.exceptions import APIException
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def register(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        try:
            CustomUser.objects.create_user(username=username, email=email, password=password)
        except Exception:
            raise APIException(
                "User with same username already exists",
                code="400;%s" % "USER_ALREADY_EXISTS",
            )

        return Response({
            "msg": "User succesfully created"
        })

    def profile(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(pk=request.user.id)
        except Exception:
            raise APIException(
                "User not found",
                code="400;%s" % "CANT FIND USER",
            )
        serializer = self.get_serializer(user)
        data = serializer.data

        return Response(data)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        print(request.headers)
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.headers['Authorization'])
        return Response({'token': token.key, 'id': token.user_id})


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]