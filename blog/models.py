from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    bf_link = models.TextField(max_length=100, blank=True, null=True)
    link = models.TextField(max_length=100, blank=True, null=True)
    af_link = models.TextField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'id': self.id
        })