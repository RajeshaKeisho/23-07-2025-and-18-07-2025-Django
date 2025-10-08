from django.shortcuts import render
import datetime

# Create your views here.
def wish(request):
    time = datetime.datetime.now()
    name = 'Akshay'
    age = 25
    rollno = 101
    marks = 90
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    my_dict = {"insert_date":formatted_time, 'name':name, 'age':age, 'rollno':rollno, 'marks':marks}
    return render(request, 'wish.html', my_dict)

def greet(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if now.hour < 12:
        greeting = "Good Morning!"
    elif now.hour < 16:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    return render(request, 'myapp/greet.html', {'greeting':greeting, 'time':current_time})

