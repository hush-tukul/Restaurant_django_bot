# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from jsonfield import JSONField


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class User(TimeBasedModel):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    id = models.AutoField(primary_key=True)
    user_id = models.BigIntegerField(unique=True, default=1, verbose_name="Telegram user id")
    name = models.CharField(max_length=100, verbose_name="Telegram user actual name")
    username = models.CharField(max_length=100, verbose_name="Telegram user username")
    email = models.CharField(max_length=100, verbose_name="Email", null=True)

    def __str__(self):
        return f"№{self.id} {self.user_id} - {self.name}"


class Referral(TimeBasedModel):
    class Meta:
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"

    id = models.ForeignKey(
        User,
        primary_key=True,
        on_delete=models.CASCADE
    )
    referrer_id = models.BigIntegerField()

    def __str__(self):
        return f"{self.id} - from {self.referrer_id}"


class Item(TimeBasedModel):
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Item name')
    photo = models.CharField(max_length=200, verbose_name='Item photo file_id')
    price = models.DecimalField(verbose_name='Price', decimal_places=2, max_digits=8)
    description = models.TextField(verbose_name='Description', max_length=3000, null=True)

    category_code = models.CharField(max_length=20, verbose_name='Category Code')
    category_name = models.CharField(max_length=20, verbose_name='Category Name')
    subcategory_code = models.CharField(max_length=20, verbose_name='Subcategory Code')
    subcategory_name = models.CharField(max_length=20, verbose_name='Subcategory Name')

    def __str__(self):
        return f"№{self.id} - {self.name}"


class Purchase(TimeBasedModel):
    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(User, verbose_name='Buyer', on_delete=models.SET(0))
    item_id = models.ForeignKey(Item, verbose_name='Item ID', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, verbose_name='Amount', decimal_places=2)
    quantity = models.IntegerField(verbose_name='Quantity')
    purchase_time = models.DateTimeField(verbose_name='Purchase Time', auto_now_add=True)
    shipping_address = JSONField(verbose_name="Shipping Address", null=True)
    phone_number = models.CharField(max_length=50, verbose_name="Phone Number")
    email = models.CharField(max_length=100, verbose_name='Email Address', null=True)
    receiver = models.CharField(max_length=100, verbose_name='Receiver Name', null=True)
    successful = models.BooleanField(verbose_name='Successfull payment', default=False)

    def __str__(self):
        return f"№{self.id} - {self.item_id} ({self.quantity})"




















