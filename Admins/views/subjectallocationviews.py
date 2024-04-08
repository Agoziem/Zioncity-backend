from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *



# /////////////////////////////////////////////////////////////////////////////////////////

# Subject Allocation views
@api_view(['GET'])
def getSubjectAllocations(request, school_id):
    try:
        school = School.objects.get(id=school_id)
        subjectAllocations = Subjectallocation.objects.filter(school=school)
        serializer = SubjectallocationSerializer(subjectAllocations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except School.DoesNotExist:
        return Response('School not found', status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def getSubjectAllocation(request,school_id, subjectallocation_id):
    try:
        subjectAllocation = Subjectallocation.objects.get(id=subjectallocation_id)
        serializer = SubjectallocationSerializer(subjectAllocation, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Subjectallocation.DoesNotExist:
        return Response('Subject Allocation not found', status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createSubjectAllocation(request, school_id):
    data = request.data
    subjectsid = data.get('subjects', [])
    subjects= Subject.objects.filter(id__in=subjectsid)
    try:
        school = School.objects.get(id=school_id)
        class_ = Class.objects.get(id=data['class'])
        subjectAllocation = Subjectallocation.objects.create(
            school=school,
            classname= class_
        )
        subjectAllocation.subjects.add(*subjects)
        serializer = SubjectallocationSerializer(subjectAllocation, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(str(e))
        return Response('Subject Allocation not created and error occurred', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def updateSubjectAllocation(request, subjectallocation_id):
    data = request.data
    print(data)
    try:
        subjectAllocation = Subjectallocation.objects.get(id=subjectallocation_id)
        serializer = SubjectallocationSerializer(instance=subjectAllocation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Subjectallocation.DoesNotExist:
        return Response('Subject Allocation not found', status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def deleteSubjectAllocation(request, subjectallocation_id):
    try:
        subjectAllocation = Subjectallocation.objects.get(id=subjectallocation_id)
        subjectAllocation.delete()
        return Response('Subject Allocation deleted successfully')
    except Subjectallocation.DoesNotExist:
        return Response('Subject Allocation not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////