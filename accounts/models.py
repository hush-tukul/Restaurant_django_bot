# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class TelegramUser(AbstractUser):
    chat_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name