from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from Admins.models import School

@api_view(['GET'])
def getRoutes(request):
    routes = [
        "teachersapi/<int:school_id>/",  # get all teachers based on the School ID and Class ID
        "teachersapi/create/<int:school_id>/",  # create a teacher based on the School ID and Class ID
        "teachersapi/<int:teacher_id>/",  # get a teacher based on his/her Teacher ID
        "teachersapi/<int:teacher_id>/update/",  # update a teacher based on his/her Teacher ID
        "teachersapi/<int:teacher_id>/delete/",  # delete a teacher based on his/her Teacher ID
    ]
    return Response(routes)


@api_view(['GET'])
def getTeachers(request, school_id):
    teachers = Teacher.objects.filter(school=school_id)
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTeacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    serializer = TeacherSerializer(teacher, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTeacher(request, school_id, class_id):
    data = request.data
    school = School.objects.get(id=school_id)
    teacher = Teacher.objects.create(
        firstName=data['firstName'],
        lastName=data['lastName'],
        phone_number=data['phone_number'],
        email=data['email'],
        role=data['role'],
        subjects_taught=data['subjects_taught'],
        classes_taught=data['classes_taught'],
        classFormed=data['classFormed'],
        school=school_id,
    )
    serializer = TeacherSerializer(teacher, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateTeacher(request, teacher_id):
    data = request.data
    teacher = Teacher.objects.get(id=teacher_id)
    serializer = TeacherSerializer(instance=teacher, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTeacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher.delete()
    return Response('Teacher deleted')