from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=100)
    esal = models.FloatField()
    eaddrr = models.CharField(max_length=200)

    def __str__(self):
        return f'Employee Object with E-No: {self.eno}'