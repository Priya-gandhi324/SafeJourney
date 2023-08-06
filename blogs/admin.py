from django.contrib import admin
from .models import BlogPost, Subscribers

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Subscribers)