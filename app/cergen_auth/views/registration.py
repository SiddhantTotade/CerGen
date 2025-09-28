from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from django.conf import settings

from ..renderers import UserRenderer
from ..serializers.registration import UserRegistrationSerializer


class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        response = Response({"access": access_token, "refresh": refresh_token})

        response.set_cookie(
            "access",
            access_token,
            max_age=settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )
        response.set_cookie(
            "refresh",
            refresh_token,
            max_age=settings.SIMPLE_JWT["AUTH_COOKIE_MAX_AGE"],
            path=settings.SIMPLE_JWT["AUTH_COOKIE_PATH"],
            secure=settings.SIMPLE_JWT["AUTH_COOKIE_SECURE"],
            httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
            samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
        )

        return response