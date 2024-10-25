from common_imports import *
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

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
