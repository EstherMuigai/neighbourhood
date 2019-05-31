from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')

def timeline(request):
    return render(request, 'timeline.html')
