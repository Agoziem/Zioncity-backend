from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Teacher
from .serializers import TeacherSerializer
from Admins.models import School, Class, Subject
from rest_framework import status


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

# confirm teacher Id
@api_view(['POST'])
def confirmTeacher(request):
    data = request.data
    try:
        teacher = Teacher.objects.get(id=data.get('id',''))
        if teacher.teachers_id == data.get('password',''):
            serializer = TeacherSerializer(teacher, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Teacher does not exist', status=status.HTTP_404_NOT_FOUND)
    except Teacher.DoesNotExist:
        return Response('Teacher does not exist', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getTeachers(request, school_id):
    try:
        school = School.objects.get(id=school_id)
        teachers = Teacher.objects.filter(school=school)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except School.DoesNotExist:
        return Response('School does not exist', status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def getTeacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        serializer = TeacherSerializer(teacher, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Teacher.DoesNotExist:
        return Response('Teacher does not exist', status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def createTeacher(request, school_id):
    data = request.data
    try:
        school = School.objects.get(id=school_id)
        teacher = Teacher.objects.create(
            firstName=data.get('firstName',''),
            surname=data.get('surname',''),
            sex = data.get('sex',''),
            phone_number=data.get('phone_number',''),
            email=data.get('email',''),
            role=data.get('role',''),
            headshot = data.get('headshot',''),
            address = data.get('address',''),
            school=school,
        )
        try:
            # assign the class the teacher is forming
            classid = data.get('classFormed')
            is_formteacher = data.get('is_formteacher')
            if is_formteacher and classid:
                classFormed = Class.objects.get(id=classid)
                teacher.is_formteacher = is_formteacher
                teacher.classFormed = classFormed
            else:
                classFormed = None
                teacher.is_formteacher = False
                teacher.classFormed = classFormed
            
            # assign the classes the teacher is teaching
            classes_taughtid = data.get('classes_taught',[])
            if classes_taughtid:
                classes_taught = Class.objects.filter(id__in=classes_taughtid)
                teacher.classes_taught.add(*classes_taught)
            
            # assign the subjects the teacher is teaching
            subjects_taughtid = data.get('subjects_taught',[])
            if subjects_taughtid:
                subjects_taught = Subject.objects.filter(id__in=subjects_taughtid)
                teacher.subjects_taught.add(*subjects_taught)
        except Class.DoesNotExist:
            return Response('Classformed does not exist', status=status.HTTP_404_NOT_FOUND)

        teacher.save()
        serializer = TeacherSerializer(teacher, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response("A user with the same Firstname & Lastname already exist", status=status.HTTP_404_NOT_FOUND)



# view for updating the Teachers details
@api_view(['PUT'])
def updateTeacher(request, teacher_id):
    data = request.data
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        try:
            school_id = data('school','').get('id')
            school = School.objects.get(id=school_id)
            teacher.school = school
        except:
            pass
        
        is_formteacher = data.get('is_formteacher')
        try:
            classid = data.get('classFormed', "").get('id')
        except:
            classid = None

        if is_formteacher and classid:
            classFormed = Class.objects.get(id=classid)
            teacher.is_formteacher = is_formteacher
            teacher.classFormed = classFormed
        else:
            classFormed = None
            teacher.is_formteacher = False
            teacher.classFormed = classFormed

        # update the teachers classes field
        classes_taught_data = data.get('classes_taught', [])
        if classes_taught_data:
            classes_taught_ids = [class_obj['id'] for class_obj in classes_taught_data]
            classes_taught = Class.objects.filter(id__in=classes_taught_ids)
            teacher.classes_taught.set(classes_taught)

        subjects_taught_data = data.get('subjects_taught', [])
        if subjects_taught_data:
            subjects_taught_ids = [subject_obj['id'] for subject_obj in subjects_taught_data]
            subjects_taught = Subject.objects.filter(id__in=subjects_taught_ids)
            teacher.subjects_taught.set(subjects_taught)

        # update other fields
        other_fields = ['firstName', 'surname','sex', 'phone_number', 'email', 'role','headshot',"address"]
        for field in other_fields:
            if field in data:
                setattr(teacher, field, data[field])
        teacher.save()
        serializer = TeacherSerializer(teacher, many=False)
        return Response(serializer.data)
    except Teacher.DoesNotExist:
        return Response('Teacher does not exist', status=status.HTTP_404_NOT_FOUND)




@api_view(['DELETE'])
def deleteTeacher(request, teacher_id):
    try:
        teacher = Teacher.objects.get(id=teacher_id)
        teacher.delete()
        return Response('Teacher deleted Successfully')
    except Teacher.DoesNotExist:
        return Response('Teacher does not exist', status=status.HTTP_404_NOT_FOUND)
    