from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# Create a PersonalChatRoom
@api_view(['POST'])
def createPersonalChatRoom(request):
    data = request.data
    try:
        user1 = User.objects.get(id=data.get('user1',''))
        user2 = User.objects.get(id=data.get('user2',''))
        serializer = PersonalChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save(user1=user1, user2=user2)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)

# delete the PersonalChatRoom
@api_view(['DELETE'])
def deletePersonalChatRoom(request, personalchatroom_id):
    try:
        personalchatroom = PersonalChatRoom.objects.get(id=personalchatroom_id)
    except PersonalChatRoom.DoesNotExist:
        return Response('PersonalChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)
    personalchatroom.delete()
    return Response('PersonalChatRoom deleted', status=status.HTTP_200_OK)

# get all PersonalChatRooms
@api_view(['GET'])
def getPersonalChatRooms(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        personalchatrooms = PersonalChatRoom.objects.filter(user1=user)
        serializer = PersonalChatRoomSerializer(personalchatrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response('User does not exist', status=status.HTTP_404_NOT_FOUND)

# get a PersonalChatRoom
@api_view(['GET'])
def getPersonalChatRoom(request, personalchatroom_id):
    try:
        personalchatroom = PersonalChatRoom.objects.get(id=personalchatroom_id)
        serializer = PersonalChatRoomSerializer(personalchatroom, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PersonalChatRoom.DoesNotExist:
        return Response('PersonalChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)
    

# get all PersonalChatMessages
@api_view(['GET'])
def getPersonalChatMessages(request, personalchatroom_id):
    try:
        personalchatroom = PersonalChatRoom.objects.get(id=personalchatroom_id)
        personalchatmessages = PersonalChatMessage.objects.filter(personalchatroom=personalchatroom)
        serializer = PersonalChatMessageSerializer(personalchatmessages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PersonalChatRoom.DoesNotExist:
        return Response('PersonalChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)

