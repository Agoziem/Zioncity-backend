from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *


# view to get all the newsletter in a school
@api_view(['GET'])
def get_newsletters(request, school_id):
    try:
        school_id = School.objects.get(id=school_id)
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    school_id = School.objects.get(id=school_id)
    newsletters = Newsletter.objects.filter(school=school_id)
    serializer = NewsletterSerializer(newsletters, many=True)
    return Response(serializer.data)


# view to get all the newsletter for a particular session & term
@api_view(['GET'])
def get_newsletter(request, session_id, term_id):
    try:
        session = AcademicSession.objects.get(id=session_id)
        term = Term.objects.get(id=term_id)
    except AcademicSession.DoesNotExist:
        return Response('Session not found', status=status.HTTP_404_NOT_FOUND)
    except Term.DoesNotExist:
        return Response('Term not found', status=status.HTTP_404_NOT_FOUND)
    newsletters = Newsletter.objects.filter(Newslettersession=session, Newsletterterm=term)
    serializer = NewsletterSerializer(newsletters, many=False)
    return Response(serializer.data)

# view to add a newsletter to a particular session & term
@api_view(['POST'])
def add_newsletter(request, session_id, term_id):
    try:
        session = AcademicSession.objects.get(id=session_id)
        term = Term.objects.get(id=term_id)
    except AcademicSession.DoesNotExist:
        return Response('Session not found', status=status.HTTP_404_NOT_FOUND)
    except Term.DoesNotExist:
        return Response('Term not found', status=status.HTTP_404_NOT_FOUND)
    serializer = NewsletterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(Newslettersession=session, Newsletterterm=term)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to update a newsletter
@api_view(['PUT'])
def update_newsletter(request, newsletter_id):
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
    except Newsletter.DoesNotExist:
        return Response('Newsletter not found', status=status.HTTP_404_NOT_FOUND)
    serializer = NewsletterSerializer(instance=newsletter, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# view to delete a newsletter
@api_view(['DELETE'])
def delete_newsletter(request, newsletter_id):
    try:
        newsletter = Newsletter.objects.get(id=newsletter_id)
    except Newsletter.DoesNotExist:
        return Response('Newsletter not found', status=status.HTTP_404_NOT_FOUND)
    newsletter.delete()
    return Response('Newsletter deleted', status=status.HTTP_200_OK)