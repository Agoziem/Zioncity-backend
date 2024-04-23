from ..models import *
from Students.models import Student
from Students.serializers import StudentSerializer
from Admins.models import Class,Subject,AcademicSession,Term
from ..serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# view for getting all the api routes
@api_view(['GET'])
def getRoutes(request):
    routes = [
        # for getting results

        '/getresultsummary/',
        '/getsubjectresult/',
        '/getsubjectresults/',
        '/getannualresultsummary/',
        '/getannualsubjectresult/',
        '/getannualsubjectresults/',

        # for creating results
        '/getResults/',
        '/updateResult/<int:result_id>',
        '/deleteResult/<int:result_id>',
        '/postResults/',

        '/getResultSummaries/',
        '/postResultSummaries/',

        '/getAnnualResults/',
        '/updateAnnualResult/<int:result_id>',
        '/postAnnualResults/',

        '/getAnnualResultSummaries/',
        '/postAnnualResultSummaries/',
    ]
    return Response(routes)


# view for getting one Subject result for a Student Result
@api_view(['POST'])
def get_subject_result(request):
    data=request.data
    try:
        student = Student.objects.get(id=data['student_id'])
        term = Term.objects.get(id=data['term_id'])
        session = AcademicSession.objects.get(id=data['session_id'])
        subject = Subject.objects.get(id=data['subject_id'])
        results = SubjectResult.objects.get(student=student, Subject=subject, Term=term,AcademicSession=session)
        serializer = SubjectResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except SubjectResult.DoesNotExist:
        return Response({'message': 'Subject Result does not exist'}, status=status.HTTP_404_NOT_FOUND)

# view for getting all Subject results for a Student Result
@api_view(['POST'])
def get_subject_results(request):
    data=request.data
    Result = {}
    try:
        student = Student.objects.get(id=data['student_id'],student_pin=data['student_pin'])
        term = Term.objects.get(id=data['term_id'])
        session = AcademicSession.objects.get(id=data['session_id'])
        resultsummaryobject = ResultSummary.objects.get(Student_name=student,Term=term,AcademicSession=session)
        resultsummaryserializer = ResultSummarySerializer(resultsummaryobject, many=False)
        resultsummary = resultsummaryserializer.data
        subjectresults = []
        results = SubjectResult.objects.filter(student=student, Term=term,AcademicSession=session)
        for result in results:
            serializer = SubjectResultSerializer(result, many=False)
            subjectresults.append(serializer.data)
        Result['resultsummary'] = resultsummary
        Result['subjectresults'] = subjectresults
        return Response(Result, status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response({'message': 'incorrect Credentials'}, status=status.HTTP_404_NOT_FOUND)

# //////////////////////////////////////////// Annual Results ////////////////////////////////////////////

@api_view(['POST'])
def get_annual_result_summary(request):
    data=request.data
    try:
        student = Student.objects.get(id=data['student_id'])
        session = AcademicSession.objects.get(id=data['session_id'])
        results = AnnualResultSummary.objects.get(Student_name=student,AcademicSession=session)
        serializer = AnnualResultSummarySerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AnnualResultSummary.DoesNotExist:
        return Response({'message': 'Annual Result does not exist'}, status=status.HTTP_404_NOT_FOUND)

# view for getting one Subject annual result for a Student
@api_view(['POST'])
def get_annual_subject_result(request):
    data=request.data
    try:
        student = Student.objects.get(id=data['student_id'])
        subject = Subject.objects.get(id=data['subject_id'])
        session = AcademicSession.objects.get(id=data['session_id'])
        results = AnnualSubjectResult.objects.get(student=student,Subject=subject,AcademicSession=session)
        serializer = AnnualSubjectResultSerializer(results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except AnnualSubjectResult.DoesNotExist:
        return Response({'message': 'Annual Subject Result does not exist for the Student'}, status=status.HTTP_404_NOT_FOUND)

# view for getting all Subject annual results for a Student
@api_view(['POST'])
def get_annual_subject_results(request):
    data=request.data
    try:
        student = Student.objects.get(id=data['student_id'])
        session = AcademicSession.objects.get(id=data['session_id'])
        annualsubjectresults = []
        results = AnnualSubjectResult.objects.filter(student=student, AcademicSession=session)
        for result in results:
            serializer = AnnualSubjectResultSerializer(result, many=False)
            annualsubjectresults.append(serializer.data)
        return Response(annualsubjectresults, status=status.HTTP_200_OK)
    except AnnualSubjectResult.DoesNotExist:
        return Response({'message': 'Annual Subject Results do not exist for the Student'}, status=status.HTTP_404_NOT_FOUND)
    