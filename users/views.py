
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, UserResetPasswordSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserResetPasswordView(APIView):
    serializer_class = UserResetPasswordSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        pass
