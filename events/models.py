from django.db import models
from Community.models import Community

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200, unique=True)
    slug        = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=200, blank=True)
    price       = models.IntegerField()
    images      = models.ImageField(upload_to='photos/events')
    stock       = models.IntegerField()
    is_available = models.BooleanField(default=True)
    community    = models.ForeignKey(Community, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name
