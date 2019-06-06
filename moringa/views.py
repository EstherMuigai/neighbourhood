from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ProfileForm,ProjectForm,ProjectPictures
from .models import Profile,Project,ProjectPictures

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user=request.user
    projects=Project.objects.all()
    pics=ProjectPictures.objects.all()
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        projectform = ProjectForm(request.POST, request.FILES)
        pictureform = ProjectPictures(request.POST, request.FILES)
        picture1form = ProjectPictures(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        if projectform.is_valid():
            project = projectform.save(commit=False)
            project.user = current_user
            project.save()       
    else:
        form = ProfileForm()
        projectform = ProjectForm()
        pictureform = ProjectPictures
        picture1form = ProjectPictures
    return render(request, 'profile.html',{"form":form,"projectform":projectform,"pictureform":pictureform,"projects":projects,"picture1form":picture1form,"pics":pics})

def timeline(request):
    projects=Project.objects.all()
    pics=ProjectPictures.objects.all()
    profiles=Profile.objects.all()
    return render(request, 'timeline.html',{"projects":projects,"profiles":profiles,"pics":pics})
