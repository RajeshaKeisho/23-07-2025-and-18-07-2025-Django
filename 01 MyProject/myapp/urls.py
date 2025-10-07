from django.urls import path
from .views import morning_message, noon_message, evening_message

urlpatterns = [
    path('morning/', morning_message),
    path('noon/', noon_message),
    path('evening/', evening_message)
]
