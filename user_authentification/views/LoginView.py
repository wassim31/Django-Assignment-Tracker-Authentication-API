import logging
from datetime import timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from serializers import LoginSerializer

logger = logging.getLogger(__name__)



class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        logger.info(f"Token requested for user: {request.data.get('username')}")

        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
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

