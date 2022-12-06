import datetime
import random

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20)
    citizenship = models.CharField(max_length=20, default="кыргызстан")
    birth_year = models.DateField()
    work_place = models.CharField(max_length=30, null=True, blank=True)
    update_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'customers'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.IntegerField(unique=True)
    account_type = models.IntegerField(default=1, null=False)
    client = models.ForeignKey(Client, related_name='clients', on_delete=models.CASCADE)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return f'{self.account_type}'

class Credit(models.Model):
    sum = models.IntegerField()
    date = models.DateField(default=datetime.date.today())
    account = models.ForeignKey(Account, related_name='accounts', on_delete=models.CASCADE)

    class Meta:
        db_table = 'loans'
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'

    def __str__(self):
        return self.sum




