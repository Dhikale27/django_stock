from django.db import models

# Create your models here.


class Stock(models.Model):
    ticker = models.CharField(max_length=10)

    # __str__ method required for admin
    def __str__(self):
        return self.ticker
