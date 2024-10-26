from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token


class OTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        email = data.get('email')
        otp = data.get('otp')
        try:
            user = User.objects.get(email=email, otp=otp)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP or email.")
        
        user.is_active = True
        user.otp = ''  # Clear the OTP after verification
        user.save()
        return data


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"http://frontend-url/reset-password/{uid}/{token}/"

            send_mail(
                'Password Reset',
                f'Click the link to reset your password: {reset_link}',
                'from@example.com',
                [user.email],
                fail_silently=False,
            )
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")
        
        return value


class RegisterSerializer(serializers.ModelSerializer):
    otp = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'otp']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        otp = get_random_string(length=6, allowed_chars='0123456789')
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        user.is_active = False  # Set user as inactive until OTP verification
        user.otp = otp
        user.save()

        send_mail(
            'OTP Verification',
            f'Your OTP is: {otp}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return user
