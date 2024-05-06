from rest_framework import serializers
from .models import *

# serializers for the models in the ChatSystem app
class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'

   

class RoomMessageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = RoomMessage
        fields = '__all__'
    
    def get_user(self, obj):
        return {'id': obj.user.id, 'username': obj.user.username}

class PersonalChatRoomSerializer(serializers.ModelSerializer):
    user1 = serializers.SerializerMethodField()
    user2 = serializers.SerializerMethodField()
    class Meta:
        model = PersonalChatRoom
        fields = '__all__'

    def get_user1(self, obj):
        return {'id': obj.user1.id, 'username': obj.user1.username}
    
    def get_user2(self, obj):
        return {'id': obj.user2.id, 'username': obj.user2.username}

class PersonalChatMessageSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = PersonalChatMessage
        fields = '__all__'

    def get_user(self, obj):
        return {'id': obj.user.id, 'username': obj.user.username}