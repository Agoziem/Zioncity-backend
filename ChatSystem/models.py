from django.db import models
from django.contrib.auth.models import User
from Admins.models import School

class ChatRoom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE,null=True,blank=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class RoomMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='room_messages')
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
class PersonalChatRoom(models.Model):
    name = models.CharField(max_length=100)
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='user2')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user1} and {self.user2}'
    
class PersonalChatMessage(models.Model):
    room = models.ForeignKey(PersonalChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='personal_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
