from django.db import models
from django.shortcuts import get_object_or_404
from user.models import CustomUser
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    
    def upload_path(self, filename):
        return 'user_files/{0}/{1}'.format(self.user.username, filename)

    post = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    user_file = models.FileField(upload_to=upload_path, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self, *args, **kwargs):
	    return self.post

    def get_like_url(self, *args, **kwargs):
        return reverse('likes:post-likes', kwargs={'id': self.pk})

    def get_comments(self):
        return Comment.objects.filter(post=self)
    

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    user_file = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.CharField(max_length=500, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None) #related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self, *args, **kwargs):
	    return self.comment

    

    