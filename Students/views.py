from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Admins.models import School,Class
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def getRoutes(request):
    routes = [
        "<int:school_id>/<int:class_id>/", # get students based on the School ID and Class ID
        "create/<int:school_id>/<int:class_id>/", # create a student based on the School ID and Class ID
        "<int:student_id>/", # get a student based on his/her Student ID
        "<int:student_id>/update/", # update a student based on his/her Student ID
        "<int:student_id>/delete/", # delete a student based on his/her Student ID
    ]
    return Response(routes)

# view for confirming Student id
@api_view(['POST'])
def confirmStudent(request):
    data = request.data
    try:
        student = Student.objects.get(id=data.get('id',''))
        if student.student_id == data.get('password',''):
            serializer = StudentSerializer(student, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Student does not exist', status=status.HTTP_404_NOT_FOUND)
    except Student.DoesNotExist:
        return Response('Student does not exist', status=status.HTTP_404_NOT_FOUND)
    

# get all students based on the School ID by pagination
@api_view(['GET'])
def getallStudents(request, school_id):
    try:
        paginator = PageNumberPagination()
        paginator.page_size = 21 
        school = School.objects.get(id=school_id)
        students = Student.objects.filter(student_school=school)
        result_page = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except School.DoesNotExist:
        return Response('School does not exist',status=status.HTTP_404_NOT_FOUND)
    
# get students based on the School ID and Class ID
@api_view(['GET'])
def getStudents(request, school_id, class_id):
    try:
        school = School.objects.get(id=school_id)
        student_class = Class.objects.get(id=class_id)
        students = Student.objects.filter(student_school=school, student_class=student_class)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except School.DoesNotExist or Class.DoesNotExist:
        return Response('School or Class does not exist',status=status.HTTP_404_NOT_FOUND)

# get Student based on his/her Student ID
@api_view(['GET'])
def getStudent(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response('Student does not exist',status=status.HTTP_404_NOT_FOUND)


# create a student based on the School ID and Class ID
@api_view(['POST'])
def createStudent(request,school_id, class_id):
    try:
        school = School.objects.get(id=school_id)
        student_class = Class.objects.get(id=class_id)
        data = request.data
        student = Student.objects.create(
            firstname=data.get('firstname',''),
            surname=data.get('surname',''),
            othername=data.get('othername',''),
            sex=data.get('sex',''),
            headshot=data.get('headshot',''),
            student_school=school,
            student_class=student_class,
        )
        
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data)
    except School.DoesNotExist or Class.DoesNotExist:
        return Response('School/Class does not exist in the Database',status=status.HTTP_404_NOT_FOUND)

    

# update a student based on his/her Student ID
@api_view(['PUT'])
def updateStudent(request, student_id):
    data = request.data
    try:
        student = Student.objects.get(id=student_id)
        schoolid = data.get('schoolid')
        classid = data.get('classid')

        # update the student's school and class if the school_id and class_id are provided
        try:
            if schoolid:
                school = School.objects.get(id=schoolid)
                student.student_school = school

            if classid:
                student_class = Class.objects.get(id=classid)
                student.student_class = student_class

        except School.DoesNotExist or Class.DoesNotExist:
            return Response('School/Class does not exist',status=status.HTTP_404_NOT_FOUND)

        # update the other fields
        fields_to_update = ['firstname',"surname","othername",'sex',"headshot"]
        for field in fields_to_update:
            if field in data:
                setattr(student,field,data[field])
        student.save()
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response('Student does not exist',status=status.HTTP_404_NOT_FOUND)

# delete a student based on his/her Student ID
@api_view(['DELETE'])
def deleteStudent(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
        student.delete()
        return Response('Student deleted Successfully',status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response('Student does not exist',status=status.HTTP_404_NOT_FOUND)

