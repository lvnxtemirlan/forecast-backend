from django.contrib.auth.models import AbstractUser
from backend.apps.signup.managers import CustomUserManager
from django.db import models
from django.conf import settings
import binascii
import os
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Meta:
        verbose_name_plural = 'Пользовательи'
        verbose_name = 'Пользователь'

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(_("Key"), max_length=40, primary_key=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_token',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        # Work around for a bug in Django:
        # https://code.djangoproject.com/ticket/19422
        #
        # Also see corresponding ticket:
        # https://github.com/encode/django-rest-framework/issues/705
        abstract = False
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_key(cls):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
