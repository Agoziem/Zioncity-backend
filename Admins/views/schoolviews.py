from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *



# /////////////////////////////////////////////////////////////////////////////////////////

# School views for CRUD operations
@api_view(['GET'])
def getSchools(request):
    try:
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response('No Schools found', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getSchool(request, school_id):
    try:
        school = School.objects.get(id=school_id)
        serializer = SchoolSerializer(school, many=False)
        return Response(serializer.data)
    except School.DoesNotExist:
        return Response('School not found', status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def createSchool(request):
    data = request.data
    classesid = data.get('class', [])
    classes_ = Class.objects.filter(id__in=classesid)
    sessionsid = data.get('session', [])
    sessions = AcademicSession.objects.filter(id__in=sessionsid)
    subjectsid = data.get('subject', [])
    subjects = Subject.objects.filter(id__in=subjectsid)
    try:
        school = School.objects.create(
            Schoollogo=data['Schoollogo'],
            Schoolname=data['Schoolname'],
            Schoolofficialline=data['Schoolofficialline'],
            Schoolmotto=data['Schoolmotto'],
            Schoollocation=data['Schoollocation'],
            Facebookpage=data['Facebookpage'],
            Twitterhandle=data['Twitterhandle'],
            Whatsapplink=data['Whatsapplink'],
            Emailaddress=data['Emailaddress'],
        )
        school.classes.add(*classes_)
        school.session.add(*sessions)
        school.Subjects.add(*subjects)
        serializer = SchoolSerializer(school, many=False)
        return Response(serializer.data)
    except Exception as e:
        print(str(e))
        return Response('School not created and error occurred', status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateSchool(request, school_id):
    data = request.data
    try:
        school = School.objects.get(id=school_id)
        serializer = SchoolSerializer(instance=school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except School.DoesNotExist:
        return Response('School not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteSchool(request, school_id):
    try:
        school = School.objects.get(id=school_id)
        school.delete()
        return Response('School deleted Successfully',status=status.HTTP_200_OK)
    except:
        return Response('School not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////


