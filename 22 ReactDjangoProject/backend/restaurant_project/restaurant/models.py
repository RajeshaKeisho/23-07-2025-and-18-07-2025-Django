from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    opening_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
