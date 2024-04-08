from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import *
from ..serializers import *

# /////////////////////////////////////////////////////////////////////////////////////////

# Term views
@api_view(['GET'])
def getTerms(request):
    try:
        terms = Term.objects.all()
        serializer = TermSerializer(terms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response('Terms not found', status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET'])
def getTerm(request, term_id):
    try:
        term = Term.objects.get(id=term_id)
        serializer = TermSerializer(term, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Term.DoesNotExist:
        return Response('Term not found', status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def createTerm(request):
    data = request.data
    try:
        term = Term.objects.create(term=data['term'])
        serializer = TermSerializer(term, many=False)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Exception as e:
        print(str(e))
        return Response('Term not created and error occurred', status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def updateTerm(request, term_id):
    data = request.data
    try:
        term = Term.objects.get(id=term_id)
        serializer = TermSerializer(instance=term, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Term.DoesNotExist:
        return Response('Term not found', status=status.HTTP_404_NOT_FOUND)
    

@api_view(['DELETE'])
def deleteTerm(request, term_id):
    try:
        term = Term.objects.get(id=term_id)
        term.delete()
        return Response('Term deleted', status=status.HTTP_200_OK)
    except Term.DoesNotExist:
        return Response('Term not found', status=status.HTTP_404_NOT_FOUND)

# /////////////////////////////////////////////////////////////////////////////////////////

