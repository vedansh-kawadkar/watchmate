from django.contrib import admin
from .models import Content, StreamingPlatform, Review

# Register your models here.

admin.site.register(Content)
admin.site.register(StreamingPlatform)
admin.site.register(Review)