from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student, StudentClassEnrollment
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Admins.models import AcademicSession, School,Class
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
def getallStudents(request,session_id):
    try:
        paginator = PageNumberPagination()
        paginator.page_size = 21 
        sessionobject =AcademicSession.objects.get(id=session_id)
        studentenrollment = StudentClassEnrollment.objects.filter(academic_session = sessionobject)
        students = [enrollment.student for enrollment in studentenrollment]
        result_page = paginator.paginate_queryset(students, request)
        serializer = StudentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except School.DoesNotExist:
        return Response('School does not exist',status=status.HTTP_404_NOT_FOUND)
    
# get students based on the School ID and Class ID
@api_view(['GET'])
def getStudents(request, school_id, class_id, session_id):
    try:
        school = School.objects.get(id=school_id)
        student_class = Class.objects.get(id=class_id)
        session = AcademicSession.objects.get(id=session_id)
        students = StudentClassEnrollment.objects.filter(
            student_class=student_class, academic_session=session
        ).select_related('student', 'student__student_school')
        serializer = StudentSerializer([enrollment.student for enrollment in students], many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except School.DoesNotExist or Class.DoesNotExist or AcademicSession.DoesNotExist:
        return Response('School or Class or Session does not exist',status=status.HTTP_404_NOT_FOUND)

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
def createStudent(request, school_id, class_id):
    try:
        data = request.data
        school = School.objects.get(id=school_id)
        student_class = Class.objects.get(id=class_id)
        academic_session = AcademicSession.objects.get(id=data.get("academic_session"))

        # Ensure required fields are present
        if not data.get("firstname") or not data.get("surname"):
            return Response(
                {"detail": "Firstname and Surname are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Check if the student already exists
        student, created = Student.objects.get_or_create(
            firstname=data.get("firstname").strip(),
            surname=data.get("surname").strip(),
            sex=data.get("sex", "").strip(),
            student_school=school,
            defaults={
                "othername": data.get("othername", "").strip(),
                "headshot": data.get("headshot", None),
            },
        )

        # Enroll the student in the class and session
        StudentClassEnrollment.objects.get_or_create(
            student=student,
            student_class=student_class,
            academic_session=academic_session,
        )

        # Serialize and return the student data
        serializer = StudentSerializer(student, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except (School.DoesNotExist, Class.DoesNotExist):
        return Response(
            {"detail": "School or Class does not exist in the database."},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        print(str(e))
        return Response(
            {"detail": f"An unexpected error occurred: {str(e)}"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
    

# update a student based on his/her Student ID
@api_view(['PUT'])
def updateStudent(request, student_id):
    data = request.data
    try:
        student = Student.objects.get(id=student_id)
        try:
            schoolid = data.get('schoolid','')
            school = School.objects.get(id=schoolid)
            student.student_school = school
        except:
            pass
        try:
            classid = data.get('classid','')
            student_class = Class.objects.get(id=classid)
            student.student_class = student_class
        except:
            pass
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
        StudentClassEnrollment.objects.filter(student=student).delete()
        return Response('Student deleted Successfully',status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response('Student does not exist',status=status.HTTP_404_NOT_FOUND)

