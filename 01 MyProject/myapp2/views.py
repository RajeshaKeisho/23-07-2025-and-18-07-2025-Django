import pytz
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
def greeting(request):
    current_time_utc = timezone.now()
    ist_tz = pytz.timezone("Asia/Kolkata")
    current_time_ist = current_time_utc.astimezone(ist_tz)

    hour = current_time_ist.hour

    if 6 <= hour < 12:
        greeting_message = "Good Morning!"
    elif 12 <= hour < 16:
        greeting_message = "Good Afternoon!"
    elif 16 <= hour < 21:
        greeting_message = "Good Evening!"
    else:
        greeting_message = "Good Night!"

    formatted_time = current_time_ist.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"{greeting_message} Today, the date and time in India is: {formatted_time}")
