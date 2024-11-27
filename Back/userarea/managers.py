from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self, fullname, password, email):

		if not fullname:
			raise ValueError('Users must have a name')
		
		user = self.model(fullname=fullname, email=email)
		user.set_password(password)
		
		user.save(using=self._db)
		return user

	def create_superuser(self,fullname, password, email):
		user = self.create_user(fullname=fullname,password=password,email=email)
		user.set_password(password)
		user.status = 1
		user.is_superuser = True
		user.save(using=self._db)
		return user
