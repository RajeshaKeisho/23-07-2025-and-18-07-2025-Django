from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.contrib import messages


USERS = {
    'admin':'password123',
    'user':'user123',
}

def home(request):
    username = request.session.get('username', "Guest")
    theme = request.COOKIES.get('theme', "light")
    last_activity = request.session.get('last_activity', 'no-activity-recorded')
    
    return render(request, 'home.html', {
        'username': username,   
        'theme': theme,
        'last_activity': last_activity, 
    })

def set_cookie(request):
    response = HttpResponse("Cookies have been set.")
    response.set_cookie('username', 'Rajesha')  # 1 hour
    response.set_cookie('font_size', '14px', max_age=3600)  # 1 hour
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', 'Guest')
    font_size = request.COOKIES.get('font_size', 'Not Set')
    return HttpResponse(f"Username: {username}, Font Size: {font_size}")


def set_session(request):
    request.session['user_id'] = 123
    request.session['last_activity'] = str(timezone.now())
    return HttpResponse("Session data has been set.")

def get_session(request):
    user_id = request.session.get('user_id', 'No User ID in session')
    last_activity = request.session.get('last_activity', 'No Last Activity in session')
    return HttpResponse(f"User ID: {user_id}, Last Activity: {last_activity}")


def clear_session(request):
    request.session.flush()
    return HttpResponse("Session data has been cleared.")


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if USERS.get(username) == password:
            request.session['username'] = username
            request.session['last_activity'] = str(timezone.now())
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')
    
    return render(request, 'login.html')



def set_theme(request):
    if request.method == 'POST':
        theme = request.POST.get('theme', 'light')
        response = redirect('home')
        response.set_cookie('theme', theme, max_age=30*24*60*60)  # 30 days
        return response
    return render(request, 'set_theme.html')


def protected_view(request):
    if 'username' not in request.session:
        messages.error(request, "You must be logged in to access this page.")
        return redirect('login')
    
    return HttpResponse(f"Welcome to the protected view, Only logged-in users can see this.{request.session['username']}!")

def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out.")
    return redirect('home') 

 