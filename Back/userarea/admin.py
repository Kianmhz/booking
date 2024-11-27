from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin

from .models import User
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('id','fullname' ,'email', 'user_type','is_superuser')
	list_filter =  ('user_type', 'is_superuser')
	fieldsets = (None, {'fields': ('fullname','password', 'user_type','email','last_login','date_joined')}),
	readonly_fields= ('last_login','date_joined')
	add_fieldsets = (None, {'fields': ('fullname', 'email','user_type', 'password1', 'password2')}),
	search_fields =  ('fullname', 'email')
	ordering = ('fullname',)
	list_editable = ('is_superuser','user_type')

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)