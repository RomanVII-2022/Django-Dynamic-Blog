from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    title_tag = models.CharField(max_length = 100)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    #body = models.TextField()
    created_at = models.DateField(auto_now_add = True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)


    def get_absolute_url(self):
        return reverse('home')




