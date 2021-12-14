from django.db import models

# Create your models here.

class Newsfeed(models.Model):
    body = models.TextField()
    user = models.ForeignKey('users.User', related_name='newsfeeds', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class NewsfeedFile(models.Model):
    url = models.URLField()
    FILE_TYPE_CHOICES = (
        ('image', 'image'),
        ('video', 'video'),
        ('audio', 'audio'),
        ('document', 'document'),
        ('other', 'other'),
    )
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default='other')
    newsfeed = models.ForeignKey('Newsfeed', related_name='files', on_delete=models.CASCADE)
