from django.contrib.auth.backends import ModelBackend

from django.contrib.auth import get_user_model


class Mybackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        if username and password:
            user = get_user_model().objects.filter(username=username).first()
            if user and user.check_password(password):
                return user
