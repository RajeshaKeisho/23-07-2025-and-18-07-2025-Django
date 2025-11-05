from typing import Any
from django.shortcuts import render
from .models import Product
from django.db.models import Q
from .serializers import ProductSerializer
from .filters import ProductFilter
import django_filters
from django.views.generic import ListView
from rest_framework import generics, filters


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [ django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_class = ProductFilter
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'stock']
    ordering = ['name']

