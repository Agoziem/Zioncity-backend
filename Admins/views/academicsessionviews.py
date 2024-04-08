from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *


# /////////////////////////////////////////////////////////////////////////////////////////

# Academic Session views
@api_view(['GET'])
def getAcademicSessions(request):
    try:
        academicSessions = AcademicSession.objects.all()
        serializer = AcademicSessionSerializer(academicSessions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AcademicSession.DoesNotExist:
        return Response('No Session found', status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getAcademicSession(request, session_id):
    try:
        academicSession = AcademicSession.objects.get(id=session_id)
        serializer = AcademicSessionSerializer(academicSession, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AcademicSession.DoesNotExist:
        return Response('Academic Session not found', status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createAcademicSession(request):
    data = request.data
    term_ids = data.get('terms', [])
    terms = Term.objects.filter(id__in=term_ids)
    try:
        academic_session = AcademicSession.objects.create(session=data['session'])
        academic_session.terms.add(*terms)
        serializer = AcademicSessionSerializer(academic_session)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(str(e))
        return Response('Academic Session not created and error occurred', status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['PUT'])
def updateAcademicSession(request, session_id):
    data = request.data
    try:
        academicSession = AcademicSession.objects.get(id=session_id)
        serializer = AcademicSessionSerializer(instance=academicSession, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except AcademicSession.DoesNotExist:
        return Response('Academic Session not found', status=status.HTTP_404_NOT_FOUND)
    
@api_view(['DELETE'])
def deleteAcademicSession(request, session_id):
    try:
        academicSession = AcademicSession.objects.get(id=session_id)
        academicSession.delete()
        return Response('Academic Session deleted successfully', status=status.HTTP_200_OK)
    except AcademicSession.DoesNotExist:
        return Response('Academic Session not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////


