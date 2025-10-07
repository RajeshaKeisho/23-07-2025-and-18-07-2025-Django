# from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
# def display(request):
#     s = "Hello, Students! Welcome to Django Class!"
#     return HttpResponse(s)

def morning_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Morning! Now the time is " + formatted_time + "</h1>")

def noon_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good AfterNoon! Now the time is " + formatted_time + "</h1>")

def evening_message(request):
    time = datetime.datetime.now()
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse("<h1>Hello, Good Evening! Now the time is " + formatted_time + "</h1>")