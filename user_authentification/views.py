import logging
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

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
            request.auth.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        logger.info(f"Token requested for user: {request.data.get('username')}")
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            # Add additional user info to the response if needed
            response.data['user_info'] = {
                'username': request.data.get('username'),
                'email': request.data.get('email'),
            }

        return response

    def handle_exception(self, exc):
        """Override to customize error responses."""
        logger.error(f"Token request failed: {str(exc)}")
        response = super().handle_exception(exc)
        
        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            response.data = {
                'error': 'Invalid credentials or user is inactive.',
                'status_code': response.status_code
            }
        
        return response
