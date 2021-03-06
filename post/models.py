from django.db import models
from django.shortcuts import get_object_or_404
from user.models import CustomUser
from django.urls import reverse
from imagekit.models import ImageSpecField 
from imagekit.processors import ResizeToFill

# Create your models here.

#list of choices to choose from when writing a report
REPORT_CHOICES = [
    ('Language', 'Language'),
    ('Violence', 'Violence'),
    ('Spam', 'Spam'),
    ('Harassment', 'Harassment'),
    ('Terrorism', 'Terrorism'),
    ('Hate Speech', 'Hate Speech'),
    ('Unauthorized Sales', 'Unauthorized Sales')
]
    

class Post(models.Model):
    post = models.CharField(max_length=500, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self, *args, **kwargs):
	    return self.post

    def get_like_url(self, *args, **kwargs):
        return reverse('likes:post-likes', kwargs={'id': self.pk})

    #gets the comments for each post
    def get_comments(self):
        return Comment.objects.filter(post=self)

class PostFile(models.Model):
    def upload_path(self, filename):
        return 'user_files/{0}/{1}'.format(self.user.username, filename)
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, related_name='file_posted')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    files = models.FileField(upload_to=upload_path, blank=True, null=True)
    image_thumbnail = ImageSpecField(source='files', processors=[ResizeToFill(300,230)], format='JPEG', options={'quality': 100})
    content_type = models.CharField(max_length=10, null=True)

    
#comment model
class Comment(models.Model):
    comment = models.CharField(max_length=250, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self, *args, **kwargs):
	    return self.comment
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = "Comments"

#Report model
class Report(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default = None)
    
    report_reason = models.CharField(max_length=500, null=True)
    
    report = models.CharField(
        max_length=18,
        default=1,
        choices=REPORT_CHOICES #from line 11
    )

   

    def __str__(self, *args, **kwargs):
	    return self.report
    