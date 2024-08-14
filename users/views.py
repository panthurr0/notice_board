from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer, UserResetPasswordSerializer, UserResetPasswordConfirmSerializer
from users.services import generate_password, send_email


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
        email = request.data.get("email")
        user = User.objects.get(email=email)
        uid = user.pk
        token = generate_password(8)
        user.token = token
        user.save()
        send_email(uid, token, user.email)

        return Response(
            {"success": "Письмо с восстановлением пароля отправлено"},
            status=status.HTTP_200_OK,
        )


class UserResetPasswordConfirmView(APIView):
    serializer_class = UserResetPasswordConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        uid = request.data.get("uid")
        token = request.data.get("token")
        new_password = request.data.get("new_password")

        user = User.objects.get(
            id=uid
        )
        if user.token.strip() == token.strip():
            user.set_password(new_password)
            user.token = "-"
            user.save()
            return Response(
                {"success": "Отлично! Ваш пароль обновлён"}, status=status.HTTP_200_OK
            )

        return Response(
            {"error": "Поля указаны не верно"}, status=status.HTTP_400_BAD_REQUEST
        )
