from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .functions import get_user_by_token
from django.utils import timezone
from django.contrib.auth import get_user_model

from .models import User


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

	def create(self, validated_data):
		email = validated_data['email']
		fullname = validated_data['fullname']
		password = validated_data['password']
		user_type = validated_data['user_type']

		if User.objects.filter(email=email).exists():
			raise serializers.ValidationError("Email already exists")

		if not fullname or not email or not password or not user_type:
			raise serializers.ValidationError("All fields are required")

		user = User.objects.create(fullname=fullname, email=email,user_type=user_type)
		user.set_password(password)
		user.save()
		return user



class UserInfoSerializer(serializers.ModelSerializer):
    user_type = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'fullname', 'user_type', 'date_joined', 'last_login',
                  'change_password_date', 'updated_at', 'is_superuser']

    def get_user_type(self, obj):
        return obj.get_user_type()

    def update(self, instance, validated_data):
        """
        Update user details
        """
        # Optional: Add custom validation for specific fields
        if 'email' in validated_data:
            if User.objects.filter(email=validated_data['email']).exclude(id=instance.id).exists():
                raise serializers.ValidationError({'email': 'This email is already in use.'})

        # Update user instance with validated data
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance



class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate_refresh(self, value):
        try:
            token = RefreshToken(value)
            token.blacklist()
        except Exception:
            raise ValidationError("Token is invalid or already blacklisted")
        return value

class ChangePasswordSerializer(serializers.Serializer):
	current_password = serializers.CharField(write_only=True, required=True)
	new_password = serializers.CharField(write_only=True, required=True)

	def validate(self, value):
		user = get_user_by_token(self.context['request'])
		if not user.check_password(value.get('current_password')):
			raise serializers.ValidationError({'current_password': ['Invalid password']})

		if value.get('current_password') == value.get('new_password'):
			raise serializers.ValidationError({'new_password': ['New password cannot be the same as the current password']})
		return value

	def create(self, validated_data):
		user = get_user_by_token(self.context['request'])
		user.change_password_date = timezone.now()
		user.set_password(validated_data['new_password'])
		user.save()
		return user
