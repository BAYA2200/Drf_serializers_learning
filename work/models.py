from django.db import models


# Create your models here.

class Position(models.Model):
    positions = models.CharField(max_length=50)
    departament = models.CharField(max_length=50)

    def __str__(self):
        return self.positions


class Employee(models.Model):
    full_name = models.CharField(max_length=50)
    birth_year = models.DateField()
    departament = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name