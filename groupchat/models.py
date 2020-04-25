from django.db import models
from user.models import CustomUser

class GroupChat(models.Model):
    name = models.TextField(max_length = 30)
    owner = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name='Owner')
    members = models.ManyToManyField(CustomUser)
    groupchatImage =  models.ImageField( upload_to='groupchats/', default='default.jpg', blank=True)

    @classmethod
    def add_member(cls, owner, new_member):
        member, created = cls.objects.get_or_create(
            owner=owner
        )
        member.members.add(new_member)

    @classmethod
    def remove_member(cls, owner, current_member):
        member, created = cls.objects.get_or_create(
            owner=owner
        )
        member.members.remove(new_member)
        
class GroupMessage(models.Model):
    recipient = models.ForeignKey(GroupChat,null=True, on_delete = models.CASCADE, related_name = 'GroupRecipient')
    sender = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = 'GroupSender')
    text = models.TextField(max_length = 1000)
    image = models.ImageField( upload_to='groupchat_messages/', blank=True)
    timeSent = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text
