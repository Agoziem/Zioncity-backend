from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
    
        "schools/",  # get all schools
        "schools/create/",  # create a school
        "schools/<int:school_id>/",  # get a school based on its ID
        "schools/<int:school_id>/update/",  # update a school based on its ID
        "schools/<int:school_id>/delete/",  # delete a school based on its ID

        "admins/<int:school_id>/",  # get all admins in a School based on its ID
        "admins/<int:school_id>/create/",  # create an admin in a School based on its ID
        "admins/<int:admin_id>/",  # get an admin based on his/her ID
        "admins/<int:admin_id>/update/",  # update an admin based on his/her ID
        "adminsapi/admins/<int:admin_id>/delete/",  # delete an admin based on his/her ID

        "academicsessions/",  # get all academic sessions in a school based on its ID
        "academicsessions/create/",  # create an academic session in a school based on its ID
        "academicsessions/<int:session_id>/",  # get an academic session based on its ID
        "academicsessions/<int:session_id>/update/",  # update an academic session based on its ID
        "academicsessions/<int:session_id>/delete/",  # delete an academic session based on its ID

        "terms/",  # get all terms in an academic session based on its ID
        "terms/create/",  # create a term in an academic session based on its ID
        "terms/<int:term_id>/",  # get a term based on its ID
        "terms/<int:term_id>/update/",  # update a term based on its ID
        "terms/<int:term_id>/delete/",  # delete a term based on its ID

        "classes/",  # get all classes in a school based on its ID
        "classes/create/",  # create a class in a school based on its ID
        "classes/<int:class_id>/",  # get a class based on its ID
        "classes/<int:class_id>/update/",  # update a class based on its ID
        "classes/<int:class_id>/delete/",  # delete a class based on its ID

        "subjects/<int:school_id>/",  # get all subjects in a school based on its ID
        "subjects/<int:school_id>/create/",  # create a subject in a school based on its ID
        "subjects/<int:subject_id>/",  # get a subject based
        "subjects/<int:subject_id>/update/",  # update a subject based on its ID
        "subjects/<int:subject_id>/delete/",  # delete a subject based on its ID

        "subjectallocations/<int:school_id>/",  # get all subject allocations in a school based on its ID
        "subjectallocations/<int:school_id>/create/",  # create a subject allocation in a school based on its ID
        "subjectallocations/<int:subjectallocation_id>/",  # get a subject allocation based on its ID
        "subjectallocations/<int:subjectallocation_id>/update/",  # update a subject allocation based on its ID
        "subjectallocations/<int:subjectallocation_id>/delete/",  # delete a subject allocation based on its ID
    ]
    return Response(routes)


# /////////////////////////////////////////////////////////////////////////////////////////
# confirm Admin id
@api_view(['POST'])
def confirmAdmin(request):
    data = request.data
    try:
        admin = Administrator.objects.get(id=data.get('id',''))
        if admin.admin_id == data.get('password',''):
            serializer = AdminSerializer(admin, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response('Admin not found', status=status.HTTP_404_NOT_FOUND)
    except Administrator.DoesNotExist:
        return Response('Admin not found', status=status.HTTP_404_NOT_FOUND)
    

# get school admins
@api_view(['GET'])
def getAdmins(request,school_id):
    try:
        school = School.objects.get(id=school_id)
        admins = Administrator.objects.filter(school=school)
        serializer = AdminSerializer(admins, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except School.DoesNotExist:
        return Response('School not found', status=status.HTTP_404_NOT_FOUND)

# get an admin
@api_view(['GET'])
def getAdmin(request,school_id,admin_id):
    try:
        admin = Administrator.objects.get(id=admin_id)
        serializer = AdminSerializer(admin, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Administrator.DoesNotExist:
        return Response('Admin not found', status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def createAdmin(request, school_id):
    data = request.data
    try:
        school = School.objects.get(id=school_id)
        admin = Administrator.objects.create(
            firstname=data['firstname'],
            surname=data['surname'],
            sex = data['sex'],
            adminphonenumber=data['adminphonenumber'],
            adminemail=data['adminemail'],
            headshot=data['headshot'],
            role = data['role'],
            school=school,
        )
        serializer = AdminSerializer(admin, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(str(e))
        return Response('Admin not created, school does not exist in the database', status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
def updateAdmin(request, admin_id):
    data = request.data
    try:
        admin = Administrator.objects.get(id=admin_id)
        try:
            school_id = data.get('school').get('id')
            admin.school = School.objects.get(id=school_id)
        except:
            pass   
        fields_to_update = ['firstname', 'surname','sex','adminphonenumber', 'adminemail', 'headshot', 'role']
        for field in fields_to_update:
            if field in data:
                setattr(admin, field, data[field])
        admin.save()
        serializer = AdminSerializer(admin, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Administrator.DoesNotExist:
        return Response('Admin not found', status=status.HTTP_404_NOT_FOUND)

    

@api_view(['DELETE'])
def deleteAdmin(request, admin_id):
    try:
        admin = Administrator.objects.get(id=admin_id)
        admin.delete()
        return Response('Admin deleted', status=status.HTTP_200_OK)
    except Administrator.DoesNotExist:
        return Response('Admin not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////

# 