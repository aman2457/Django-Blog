from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(verbose_name ="Blog Content")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
            return self.title
    def publish(self):
            self.published_date = timezone.now()
            self.save()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)        

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(verbose_name ='Your Name(Not Username)',max_length=200)
    text = models.TextField(verbose_name ='Comment')
    email = models.EmailField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

        