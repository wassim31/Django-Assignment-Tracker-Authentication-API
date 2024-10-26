from django.urls import path
from views import RegisterView, OTPVerificationView, LoginView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/verify-otp/', OTPVerificationView.as_view(), name='verify_otp'),
    path('api/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/token/', LoginView.as_view(), name='token_obtain_pair'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]