from django.contrib import admin
from .models import Newsfeed, NewsfeedFile
# Register your models here.

admin.site.register(Newsfeed)
admin.site.register(NewsfeedFile)
