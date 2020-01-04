from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return  reverse('post-detail', kwargs={'pk':self.pk})





class Post_like(models.Model):
    u_id = models.IntegerField()
    p_id = models.IntegerField()

