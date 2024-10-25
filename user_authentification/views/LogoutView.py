from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Blacklist the current token
            request.auth.blacklist()
            return Response({"detail": "Successfully logged out."}, status=205)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)
