from django.contrib import admin
from .models import Customer, Address, Category, Product, Order

admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
