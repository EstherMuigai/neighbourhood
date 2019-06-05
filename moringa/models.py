from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/')
    bio = models.CharField(max_length = 255)
    job = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username}'

class features(models.Model):
    feature = models.CharField(max_length =255,blank=False,null=False)

    def __str__(self):
        return self.feature

class Project(models.Model):
    project = models.CharField(max_length =255,blank=False,null=False)
    codelink = models.CharField(max_length =255,blank=False,null=False)
    description = models.CharField(max_length =255,blank=False,null=False)
    sitelink = models.CharField(max_length =255,blank=False,null=False)
    published = models.DateField("Date",blank=False,null=False)
    features = models.ManyToManyField(features)

    def __str__(self):
        return self.project

class ProjectPictures(models.Model):
    name = models.CharField(max_length =255,blank=True,null=True)
    pic = models.ImageField(upload_to = 'projects/',blank =True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Score(models.Model):
    category = models.CharField(max_length =255,blank=False,null=False)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.category
