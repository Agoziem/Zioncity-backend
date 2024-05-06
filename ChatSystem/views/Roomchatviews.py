from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# Create a ChatRoom
@api_view(['POST'])
def createChatRoom(request,school_id):
    data = request.data
    try:
        school = School.objects.get(id=school_id)
        serializer = ChatRoomSerializer(data=data)
        if serializer.is_valid():
            serializer.save(school=school)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except School.DoesNotExist:
        return Response('School does not exist', status=status.HTTP_404_NOT_FOUND)
    
# edit the ChatRoom
@api_view(['PUT'])
def editChatRoom(request, chatroom_id):
    try:
        chatroom = ChatRoom.objects.get(id=chatroom_id)
    except ChatRoom.DoesNotExist:
        return Response('ChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)
    serializer = ChatRoomSerializer(instance=chatroom, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete the ChatRoom
@api_view(['DELETE'])
def deleteChatRoom(request, chatroom_id):
    try:
        chatroom = ChatRoom.objects.get(id=chatroom_id)
    except ChatRoom.DoesNotExist:
        return Response('ChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)
    chatroom.delete()
    return Response('ChatRoom deleted', status=status.HTTP_200_OK)

# get all ChatRooms
@api_view(['GET'])
def getChatRooms(request, school_id):
    try:
        school = School.objects.get(id=school_id)
        chatrooms = ChatRoom.objects.filter(school=school)
        serializer = ChatRoomSerializer(chatrooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except School.DoesNotExist:
        return Response('School does not exist', status=status.HTTP_404_NOT_FOUND)
    
# get a ChatRoom
@api_view(['GET'])
def getChatRoom(request, chatroom_id):
    try:
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        serializer = ChatRoomSerializer(chatroom, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ChatRoom.DoesNotExist:
        return Response('ChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)

# get all messages in a ChatRoom
@api_view(['GET'])
def getRoomMessages(request, chatroom_id):
    try:
        chatroom = ChatRoom.objects.get(id=chatroom_id)
        messages = RoomMessage.objects.filter(room=chatroom)
        serializer = RoomMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ChatRoom.DoesNotExist:
        return Response('ChatRoom does not exist', status=status.HTTP_404_NOT_FOUND)
    
