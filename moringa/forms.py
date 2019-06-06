from .models import Profile,Project,Score,ProjectPictures,features
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        exclude = ['project']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']

class ProjectPictures(forms.ModelForm):
    class Meta:
        model = ProjectPictures
        exclude = ['project']