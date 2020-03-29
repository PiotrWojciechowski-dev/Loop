from django.db import models
from user.models import CustomUser

class Message(models.Model):
    recipient = models.ForeignKey(CustomUser,null=True, on_delete = models.CASCADE, related_name = 'recipient')
    sender = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'sender')
    text = models.TextField(max_length = 1000)
    image = models.ImageField( upload_to='messages/', blank=True)
    sent = models.DateTimeField(auto_now_add = True)
    unread = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
