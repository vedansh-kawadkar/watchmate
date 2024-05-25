from django.db import models

# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    created= models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return self.name