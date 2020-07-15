from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(verbose_name ="Title for Your Blog", max_length=200)
    text = models.TextField(verbose_name ="Blog Content",)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    post_views=models.IntegerField(default=0)
    likes =models.ManyToManyField(User, related_name='likes',blank=True)
    def __str__(self):
            return self.title
    def publish(self):
            self.published_date = timezone.now()
            self.save()
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True) 
     
    def get_absolute_url(self):
            return reverse('post_detail', kwargs={'pk':self.pk}) 

    def total_likes(self):
            return self.likes.count()                   

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(verbose_name ='Your Name(Not Username)',max_length=200)
    text = models.TextField(verbose_name ='Comment')
    email = models.EmailField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)


    def __str__(self):
        return self.text

    def total_comments(self):
            return self.approved_comment.count()     

        