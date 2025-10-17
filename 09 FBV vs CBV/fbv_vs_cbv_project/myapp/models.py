from django.db import models
from django.utils import timezone
# Create your models here.
class  Item(models.Model):
    CATEGORY_CHOICES = [
        ('ELE', 'Electronics'),
        ('FUR', 'Furniture'),
        ('CLO', 'Clothing'),
        ('TOY', 'Toys'),
        ('OTH', 'Other'),
    ]
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name