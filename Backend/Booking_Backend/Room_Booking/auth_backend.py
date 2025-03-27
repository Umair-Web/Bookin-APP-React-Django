from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
# it is built in authentication backend that provides default authentication logic
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest

# Below is our custom authenticate backend since we are using email to authenticate users ,here the username will be email
class EmailBackend(ModelBackend):
    def authenticate(self, request, username =None, password =None, **kwargs):
        UserModel=get_user_model()
        try:
            user=UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
            return None
