from django.db import models

# Create your models here.

class Smartphone (models.Model):
    brand = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.brand + ' - ' + str(self.price) + 'TND'
