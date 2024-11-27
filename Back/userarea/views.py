from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.exceptions import NotAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UsersSerializer, UserInfoSerializer, LogoutSerializer, ChangePasswordSerializer
from .permissions import AllowAnyUser, IsAuthenticatedUser
from .functions import get_user_by_token
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserInfoSerializer



class RegisterView(APIView):
	permission_classes = [AllowAnyUser]

	def post(self, request):
		serializer = UsersSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'message': 'User created successfully', 'status': status.HTTP_201_CREATED},
				   status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class UserProfileView(RetrieveUpdateAPIView):
    """
    View to retrieve and update user profile.
    """
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Override to fetch the user by ID from the URL.
        """
        user_id = self.kwargs.get('user_id')
        return self.queryset.get(pk=user_id)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		return token

class MyTokenObtainPairView(TokenObtainPairView):
	serializer_class = MyTokenObtainPairSerializer


#! User data
class UserInfoView(APIView):
	permission_classes = [IsAuthenticatedUser]

	def get(self, request):
		user = get_user_by_token(request)
		if user is None:
			return Response({'detail': ['Invalid credentials']}, status=status.HTTP_401_UNAUTHORIZED)
		serializer = UserInfoSerializer(user)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)


#! Refresh token
class MyRefreshTokenSerializer(TokenRefreshSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)
		return token

class MyRefreshTokenView(TokenRefreshView):
	serializer_class = MyRefreshTokenSerializer


#! Logout
class LogoutView(APIView):
	permission_classes = [IsAuthenticatedUser]

	def post(self, request):
		serializer = LogoutSerializer(data=request.data)
		if serializer.is_valid():
			return Response({'message': ['Logged out successfully'], 'status': status.HTTP_200_OK},
						status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)


class UsersChangePassword(APIView):
	permission_classes = [IsAuthenticatedUser]

	def post(self, request):
		serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
		if serializer.is_valid():
			serializer.save()
			return Response({'message': ['Password changed successfully'], 'status': status.HTTP_200_OK},
							status=status.HTTP_200_OK)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def permission_denied(self, request, message=None, code=None):
		raise NotAuthenticated(message)
