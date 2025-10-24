from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<html><body><h1>About Page</h1><p>This is the about page of the construction site.</p></body></html>")

def test_exception_view(request):
    """A view that itself does nothing."""
    pass  # intentionally no logic
    return HttpResponse("✅ View executed successfully (if no exception middleware)")