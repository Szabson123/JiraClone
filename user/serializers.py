from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        
        fields = ['id', 'nickname', 'email', 'first_name', 'last_name', 'password']
        
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must have at least 8 characters')
        else:
            return value

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()