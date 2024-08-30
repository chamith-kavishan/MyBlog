from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=100)
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")
    bio = models.TextField(blank=True)
    
    def __str__(self):
        return self.username