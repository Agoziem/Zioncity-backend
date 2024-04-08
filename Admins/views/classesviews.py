from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# /////////////////////////////////////////////////////////////////////////////////////////


# Class views
@api_view(['GET'])
def getClasses(request):
    try:
        classes = Class.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response('something went wrong while retrieving the classes', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getClass(request, class_id):
    try:
        class_ = Class.objects.get(id=class_id)
        serializer = ClassSerializer(class_, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Class.DoesNotExist:
        return Response('Class not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def createClass(request):
    data = request.data
    try:
        class_ = Class.objects.create(Class=data['class_'])
        serializer = ClassSerializer(class_, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(str(e))
        return Response('Class not created and error occurred', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateClass(request, class_id):
    data = request.data
    try:
        class_ = Class.objects.get
        serializer = ClassSerializer(instance=class_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Class.DoesNotExist:
        return Response('Class not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def deleteClass(request, class_id):
    try:
        class_ = Class.objects.get(id=class_id)
        class_.delete()
        return Response('Class deleted successfully', status=status.HTTP_200_OK)
    except Class.DoesNotExist:
        return Response('Class not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////
