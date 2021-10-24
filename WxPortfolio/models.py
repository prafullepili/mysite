from django.db import models


class TransactionCurrency(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Coins(models.Model):
    basename = models.CharField(max_length=100)
    fullname = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    tc = models.ForeignKey(TransactionCurrency, on_delete=models.SET_NULL, null=True)
