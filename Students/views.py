from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Admins.models import School,Class

@api_view(['GET'])
def getRoutes(request):
    routes = [
        "studentsapi/<int:school_id>/<int:class_id>/", # get students based on the School ID and Class ID
        "studentsapi/create/<int:school_id>/<int:class_id>/", # create a student based on the School ID and Class ID
        "studentsapi/<int:student_id>/", # get a student based on his/her Student ID
        "studentsapi/<int:student_id>/update/", # update a student based on his/her Student ID
        "studentsapi/<int:student_id>/delete/", # delete a student based on his/her Student ID
    ]
    return Response(routes)

# get students based on the School ID and Class ID
@api_view(['GET'])
def getStudents(request, school_id, class_id):
    school = School.objects.get(id=school_id)
    student_class = Class.objects.get(id=class_id)
    students = Student.objects.filter(student_school=school, student_class=student_class)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# get Student based on his/her Student ID
@api_view(['GET'])
def getStudent(request, student_id):
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)


# create a student based on the School ID and Class ID
@api_view(['POST'])
def createStudent(request,school_id, class_id):
    school = School.objects.get(id=school_id)
    student_class = Class.objects.get(id=class_id)
    data = request.data
    student = Student.objects.create(
        student_name=data['student_name'],
        Sex=data['Sex'],
        student_Photo=data['student_Photo'],
        student_school=school,
        student_class=student_class,
    )
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

# update a student based on his/her Student ID
@api_view(['PUT'])
def updateStudent(request, student_id):
    data = request.data
    student = Student.objects.get(id=student_id)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete a student based on his/her Student ID
@api_view(['DELETE'])
def deleteStudent(request,student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return Response('Student deleted')
