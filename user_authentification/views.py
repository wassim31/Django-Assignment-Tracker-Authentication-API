import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import RegisterSerializer, OTPVerificationSerializer, LoginSerializer

logger = logging.getLogger(__name__)

class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"detail": "Registration successful. Verify your email using the OTP."}, 
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OTPVerificationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            # Implement OTP verification logic here
            return Response({"detail": "Email verified successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the user's current token
            auth = JWTAuthentication()
            raw_token = request.META.get('HTTP_AUTHORIZATION').split()[1]
            token = OutstandingToken.objects.get(token=raw_token)
            # Blacklist the token
            BlacklistedToken.objects.create(token=token)
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        logger.info(f"Token requested for user: {request.data.get('username')}")
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            # Use validated data from the serializer to get the user details
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.user  # This should provide an authenticated user

            response.data['user_info'] = {
                'username': user.username,
                'email': user.email,
            }

        return response

