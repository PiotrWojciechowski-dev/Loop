from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    body = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    

    