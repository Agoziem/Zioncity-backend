from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# get all the notifications for a particular school
@api_view(['GET'])
def get_notifications(request, school_id):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    notifications = Notification.objects.filter(school=school)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# get all the notifications for a user_group
@api_view(['GET'])
def get_notifications_by_group(request, school_id, user_group):
    try:
        school = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    notifications = Notification.objects.filter(school=school, Notification_group=user_group).order_by('-id')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# get a Single notification
@api_view(['GET'])
def get_single_notification(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = NotificationSerializer(notification)
    return Response(serializer.data, status=status.HTTP_200_OK)


# create a Notification
@api_view(['POST'])
def create_notification(request, school_id):
    try:
        school = School.objects.get(id=school_id)
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(school=school)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# update a Notification
@api_view(['PUT'])
def update_notification(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        serializer = NotificationSerializer(instance=notification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
# delete a Notification
@api_view(['DELETE'])
def delete_notification(request, notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        notification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)