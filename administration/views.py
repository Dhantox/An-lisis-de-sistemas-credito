from django.shortcuts import render
from django.shortcuts import render_to_response
from .import views
# Create your views here.
def signup_view(request):
    return render(request,'users/signup.html')
