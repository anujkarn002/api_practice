from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', null=True, on_delete=models.CASCADE)

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    phone = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    )
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=20)
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

