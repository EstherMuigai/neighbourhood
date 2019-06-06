from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')

def timeline(request):
    return render(request, 'timeline.html')
