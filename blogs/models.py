from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class BlogPost(TimeStampedModel):
    image = models.ImageField(upload_to='static/images/')
    place = models.TextField(max_length=100)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    experience = models.TextField(max_length=1000)


class Subscribers(TimeStampedModel):
    name = models.TextField(max_length=100)
    email = models.EmailField()