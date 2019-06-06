from django.db import models
from django.contrib.auth.models import User

class Neighbourhood(models.Model):
    HOODS = (
        ('South B','South B'),
        ('Makongeni','Makongeni'),
        ('Kileleshwa','Kileleshwa'),
    )
    neighbourhood = models.CharField(max_length=1,choices=HOODS)
    pic = models.ImageField(blank=True,upload_to = 'hoods/')

    def __str__(self):
        return f'{self.name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'images/',default = 'images/beauty1.jpg')
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,blank=True,null=True)
    bio = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username}'

