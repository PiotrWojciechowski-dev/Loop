from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    body = models.TextField(),
    date = models.DateField(),

    def __str__(self):
        return self.author

    