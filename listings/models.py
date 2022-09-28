from django.db import models

# Create your models here
MODELS_TYPES = (
     ('bmw', 'bmw'),
     ('audi', 'audi'),
     ('volkswagen', 'volkswagen')
)

class Listing(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    brand = models.CharField(verbose_name='Models', max_length=10, choices=MODELS_TYPES)
    milage = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name
