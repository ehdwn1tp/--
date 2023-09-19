from django.db import models

# Create your models here.
class Coffee(models.Model):
    name = models.CharField(default='', primary_key=True, max_length=20)
    price = models.SmallIntegerField(default=0)
    drink_kind = models.CharField(default='', max_length=20)
    stock = models.SmallIntegerField(default=0)


    def __str__(self):
        return self.name
