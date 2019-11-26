from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class AccountPayment(models.Model):
    # таблица onlinepayment_accountpayment

    account_number = models.CharField(max_length=255)
    city_code = models.CharField(max_length=255)
    uniq_uuid = models.CharField(max_length=36, null=True, blank=True, unique=True)
    infougra_status = models.CharField(max_length=1000, null=True, blank=True)
    infougra_message = models.CharField(max_length=1000, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    gtnet_response = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(
        "bonus.User", null=True, blank=True, on_delete=models.SET_NULL
    )
    phone = models.CharField(max_length=100, null=True, blank=True)
    bonus_payment = models.BooleanField(default=False)
    track = models.CharField(max_length=100, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "onlinepayment_accountpayment"


class AccountPaymentService(models.Model):
    # таблица onlinepayment_accountpaymentservice
    account_payment = models.ForeignKey(AccountPayment, on_delete=models.PROTECT)
    service_name = models.CharField(max_length=255)
    supplier_name = models.CharField(max_length=255)
    service_id = models.CharField(max_length=32)
    supplier_id = models.CharField(max_length=32)
    main_sum = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    fine_sum = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    class Meta:
        db_table = "onlinepayment_accountpaymentservice"


class BonusTransaction(models.Model):
    # таблица onlinepayment_bonustransaction
    user = models.ForeignKey("bonus.User", on_delete=models.PROTECT)
    account_payment = models.ForeignKey(
        AccountPayment, null=True, blank=True, on_delete=models.PROTECT
    )
    value = models.DecimalField(max_digits=20, decimal_places=2)
    note = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateField(null=False, blank=False)
    date_updated = models.DateField(null=False, editable=False, default=timezone.now)

    class Meta:
        db_table = "onlinepayment_bonustransaction"


# AbstractUser - класс из django
class User(AbstractUser):
    # таблица users_user

    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r"\d{10}")],
        null=True,
        blank=True,
        verbose_name=u"Номер мобильного телефона",
    )
    first_time = models.BooleanField(default=True)

    class Meta:
        db_table = "users_user"
