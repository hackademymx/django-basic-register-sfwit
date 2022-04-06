from rest_framework import serializers
from users.models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'email',
            'is_active',
            'is_verified',
        ]
        extra_kwargs = {
            'password':{'write_only': True},
        }