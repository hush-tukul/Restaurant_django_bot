from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import User, Item, Purchase, Referral
# from django.contrib.auth.admin import UserAdmin
#
# from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
#
#CustomUser = get_user_model()
# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = [
#     "email",
#     "username",
#     "is_superuser",
#     ]
#
#admin.site.unregister(CustomUser)
# admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_id",
        "name",
        "username",
        "created_at",
    )


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "category_name",
        "subcategory_name",
    )


@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "referrer_id",

    )


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "buyer",
        "item_id",
        "quantity",
        "receiver",
        "created_at",
        "successful",
    )
