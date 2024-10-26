from common_imports import *


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
        user.is_active = False  
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
