from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *


# /////////////////////////////////////////////////////////////////////////////////////////


# Subject views
@api_view(['GET'])
def getSubjects(request):
    try:
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response('Subjects not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getSubject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        serializer = SubjectSerializer(subject, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Subject.DoesNotExist:
        return Response('Subject not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createSubject(request):
    data = request.data
    try:
        subject = Subject.objects.create(
            subject_code=data['subject_code'],
            subject_name=data['subject_name'],
        )
        serializer = SubjectSerializer(subject, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
        return Response('Subject not created and error occurred', status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateSubject(request,subject_id):
    data = request.data
    try:
        subject = Subject.objects.get(id=subject_id)
        serializer = SubjectSerializer(instance=subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Subject.DoesNotExist:
        return Response('Subject not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteSubject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        subject.delete()
        return Response('Subject deleted successfully', status=status.HTTP_200_OK)
    except Subject.DoesNotExist:
        return Response('Subject not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////

