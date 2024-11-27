from django.urls import path, include
from rest_framework import routers

from .views import RegisterView, MyTokenObtainPairView, UserInfoView, MyRefreshTokenView,\
					LogoutView, UsersChangePassword, UserProfileView

app_name = "userarea"
router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)),

	path('register', RegisterView.as_view(), name='register'),
	path('login', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('user-info', UserInfoView.as_view(), name='user_info'),
	path('refresh', MyRefreshTokenView.as_view(), name='refresh'),
	path('logout', LogoutView.as_view(), name='logout'),
	path('change-pass', UsersChangePassword.as_view(), name='change_pass'),
	path('user-profile/<int:user_id>/', UserProfileView.as_view(), name='user_profile'),
]
