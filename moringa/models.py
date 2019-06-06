from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/',default = 'images/beauty1.jpg')
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
    user= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    published = models.DateField("Date",blank=False,null=False)

    def __str__(self):
        return self.project

class ProjectPictures(models.Model):
    projectpicture = models.CharField(max_length =255,blank=True,null=True)
    pic = models.ImageField(upload_to = 'projects/')
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.projectpicture


class Score(models.Model):
    SCORES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
    )
    CATEGORY = (
        ('Usability', 'Usability'),
        ('Design' , 'Design'),
        ('Content' , 'Content'),
    )
    category = models.CharField(max_length=1,choices=CATEGORY)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    score = models.IntegerField(choices=SCORES)

    def __str__(self):
        return self.category
