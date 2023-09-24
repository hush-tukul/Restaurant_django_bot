from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import TelegramUserCreationForm, TelegramUserChangeForm
from .models import TelegramUser

TelegramUser = get_user_model()


class TelegramUserAdmin(UserAdmin):
    add_form = TelegramUserCreationForm
    form = TelegramUserChangeForm
    model = TelegramUser
    list_display = [
        "email",
        "username",
        "is_superuser",
    ]


admin.site.register(TelegramUser, TelegramUserAdmin)
# Register your models here.
