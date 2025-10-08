from django.urls import path
from .views import wish, greet

urlpatterns = [
    path('wish/', wish, name='wish'),
    path('greet/', greet, name='greet'),
]

