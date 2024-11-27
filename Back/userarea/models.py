from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
	USER_TYPE = (
		(1, 'customer'),
		(2, 'host'),
	)
	fullname = models.CharField(max_length=255, null=True, blank=True)
	email = models.EmailField(max_length=255, null=True, blank=True,  unique=True)
	user_type = models.IntegerField(choices=USER_TYPE, default=1)
	date_joined = models.DateTimeField(auto_now_add=True)
	last_login = models.DateTimeField(auto_now_add=True)
	change_password_date = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

	USERNAME_FIELD = 'email' # for authentication purposes
	REQUIRED_FIELDS = ['fullname', ] # just for createsuperuser

	def __str__(self):
		return f"{self.fullname} - {self.id}"

	def has_perm(self, perm, obj=None):
		return True

	def has_moduls_perms(self, app_label):
		return True

	@property
	def is_staff(self):
		return self.is_superuser

	def get_user_type(self):
		return {
			'id': int(self.user_type),
			'name': dict(User.USER_TYPE).get(self.user_type)
		}


