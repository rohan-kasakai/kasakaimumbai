from django.db import models
from django.urls import reverse

# Create your models here.

class Community(models.Model):
    Community_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    Community_image = models.ImageField(upload_to='photos/Communities', blank=True)

    class Meta:
        verbose_name = 'Community'
        verbose_name_plural = 'Communities'

    def get_url(self):
            return reverse('events_by_community', args=[self.slug])

    def __str__(self):
        return self.Community_name
