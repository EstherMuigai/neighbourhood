from django.contrib import admin
from .models import Profile,Neighbourhood,HoodDetails,Post

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(HoodDetails)
admin.site.register(Neighbourhood)
