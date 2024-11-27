from rest_framework.authentication import get_authorization_header
from rest_framework_simplejwt.tokens import AccessToken

from .models import User


def get_user_by_token(request):
	auth_header = get_authorization_header(request).split()
	if len(auth_header) != 2 or auth_header[0].lower() != b'bearer':
		return False
	try:
		token = auth_header[1].decode('utf-8')
		if token == 'null':
			return False
		access_token = AccessToken(token)
		user_id = access_token['user_id']
		user = User.objects.get(id=user_id)
		return user
	except Exception as e:
		print(e)
		return False
