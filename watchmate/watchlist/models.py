from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.
  
class StreamingPlatform(models.Model):
    name = models.CharField(max_length=20)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200)
    
    def __str__(self) -> str:
        return self.name
    
    
class Content(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)
    platform = models.ForeignKey(StreamingPlatform, on_delete=models.CASCADE, related_name='content') #1 content has 1 platforms, 1 platforms has multiple content
    
    def __str__(self) -> str:
        return self.title
    
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, null=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='review')
    
    def __str__(self):
        return f"{self.content.title} : {str(self.rating)}"