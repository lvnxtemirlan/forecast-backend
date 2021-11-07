from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(username=username, email=email, password=password, **extra_fields)


