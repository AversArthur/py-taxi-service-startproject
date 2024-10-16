from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self: 'Manufacturer') -> str:
        return f"{self.name} from {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self: 'Driver') -> str:
        return f"{self.first_name} {self.last_name}: {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver,
                                on_delete=models.SET_NULL,
                                null=True, blank=True,
                                related_name='cars')
