from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from Admins.models import *
from Students.models import Student
import json

# Create your views here.

@api_view(['GET'])
def getcreatingResultRoutes(request):
    routes = [
        '/getResults/',
        '/updateResult/<int:result_id>',
        '/deleteResult/<int:result_id>',
        '/postResults/',

        '/getResultSummaries/',
        '/postResultSummaries/',

        '/getAnnualResults/',
        '/updateAnnualResult/<int:result_id>',
        '/resultapi/postAnnualResults/',

        '/getAnnualResultSummaries/',
        '/postAnnualResultSummaries/',

    ]
    return Response(routes)

# get all results for a subject in a term and session
@api_view(['POST'])
def getResults(request):
    data = request.data
    term = Term.objects.get(id=data['term_id'])
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    subject = Subject.objects.get(id=data['subject_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    studentsubjectResults = []
    for student in studentsinclass:
        studentresult,created = SubjectResult.objects.get_or_create(student=student,student_class=student_class,Subject=subject,Term=term,AcademicSession=session)
        studentsubjectResults.append({
            'Name': studentresult.student.student_name,
            'studentID': studentresult.student.student_id,
            '1sttest': studentresult.FirstTest,
            '1stAss': studentresult.FirstAss,
            'MTT': studentresult.MidTermTest,
            '2ndTest': studentresult.SecondAss,
            '2ndAss': studentresult.SecondTest,
            'Exam': studentresult.Exam,
        })
    studentsubjectResultsjson = json.dumps(studentsubjectResults)
    return Response(studentsubjectResultsjson)


# update student result 
@api_view(['UPDATE'])
def updateResult(request, result_id):
    data = request.data
    result = SubjectResult.objects.get(id=result_id)
    serializer = SubjectResultSerializer(instance=result, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# delete student result
@api_view(['DELETE'])
def deleteResult(request, result_id):
    result = SubjectResult.objects.get(id=result_id)
    result.delete()
    return Response('Result Deleted')

# post all student subject results for a term and session
@api_view(['POST'])
def postResults(request):
    data = request.data
    term = Term.objects.get(id=data['term_id'])
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    subject = Subject.objects.get(id=data['subject_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    for student in studentsinclass:
        try:
            studentresult = SubjectResult.objects.get(student=student,student_class=student_class,Subject=subject,Term=term,AcademicSession=session)
            studentresult.FirstTest = data['FirstTest']
            studentresult.FirstAss = data['FirstAss']
            studentresult.MidTermTest = data['MidTermTest']
            studentresult.SecondAss = data['SecondAss']
            studentresult.SecondTest = data['SecondTest']
            studentresult.Exam = data['Exam']
            studentresult.Total = data['Total']
            studentresult.Grade = data['Grade']
            studentresult.SubjectPosition = data['SubjectPosition']
            studentresult.Remark = data['Remark']
            studentresult.save()
        except:
            pass
    return Response('Results Published Successfully')

# //////////////////////////////////////////// Formteachers Results Summary ////////////////////////////////////////////

# get all student results total for a term 
@api_view(['POST'])
def getResultSummaries(request):
    data = request.data
    term = Term.objects.get(id=data['term_id'])
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    classsubjectsallocations = Subjectallocation.objects.get(classname=student_class,school=school)
    studentResultSummary = []
    for student in studentsinclass:
        student_dict = {
            'Name': student.student_name,
        }
        for subject in classsubjectsallocations.subjects.all():
            try:
                subresult = SubjectResult.objects.get(student=student,student_class=student_class,Subject=subject,Term=term,AcademicSession=session)
                student_dict[subject.subject_code] = subresult.Total
            except:
                student_dict[subject.subject_code] = "-"
        studentResultSummary.append(student_dict)
    studentResultSummaryjson = json.dumps(studentResultSummary)
    return Response(studentResultSummaryjson)

# post all student results summary for a term
@api_view(['POST'])
def postResultSummaries(request):
    data = request.data
    term = Term.objects.get(id=data['term_id'])
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    for student in studentsinclass:
        studentresult,created = ResultSummary.objects.get_or_create(Student_name=student,Term=term,AcademicSession=session)
        studentresult.TotalScore = data['TotalScore']
        studentresult.Totalnumber = data['Totalnumber']
        studentresult.Average = data['Average']
        studentresult.Position = data['Position']
        studentresult.Remark = data['Remark']
        studentresult.save()
    return Response('Class Results Published Successfully, and now open for viewing')


# //////////////////////////////////////////// Teachers Annual Results ////////////////////////////////////////////
# view for creating & getting all students annual result for a subject
@api_view(['POST'])
def getAnnualResults(request):
    data = request.data
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    subjectannual = Subject.objects.get(id=data['subject_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    studentssubjectAnnualResult = []
    for student in studentsinclass:
        termlystudentresults = SubjectResult.objects.filter(student=student,student_class=student_class,Subject=subjectannual,AcademicSession=session)
        for result in termlystudentresults:
            if result.Term.term == 'First Term':
                firsttermresult = result.Total
            elif result.Term.term == 'Second Term':
                secondtermresult = result.Total
            else:
                thirdtermresult = result.Total
        annualstudentresult = AnnualSubjectResult.objects.get_or_create(Student_name=student,subject=subjectannual,AcademicSession=session)
        studentssubjectAnnualResult.append({
            'Name': annualstudentresult.Student_name.student_name,
            'studentID': annualstudentresult.Student_name.student_id,
            'FirstTermTotal':  firsttermresult,
            'SecondTermTotal': secondtermresult,
            'ThirdTermTotal': thirdtermresult,
        })
    studentssubjectAnnualResultjson = json.dumps(studentssubjectAnnualResult)
    return Response(studentssubjectAnnualResultjson)

# view for updating Student Annual Result for a Subject by the Teacher
@api_view(['UPDATE'])
def updateAnnualResult(request, result_id):
    data = request.data
    result = AnnualSubjectResult.objects.get(id=result_id)
    serializer = AnnualSubjectResultSerializer(instance=result, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# view for submitting all Students Annual Result for a Subject by the Teacher
@api_view(['POST'])
def postAnnualResults(request):
    data = request.data
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    subjectannual = Subject.objects.get(id=data['subject_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    for student in studentsinclass:
        try:
            studentresult = AnnualSubjectResult.objects.get(Student_name=student,subject=subjectannual,AcademicSession=session)
            studentresult.Total = data['Total']
            studentresult.Average = data['Average']
            studentresult.Grade = data['Grade']
            studentresult.SubjectPosition = data['SubjectPosition']
            studentresult.Remark = data['Remark']
            studentresult.save()
        except:
            pass
    return Response('Annual Results Published Successfully')


# //////////////////////////////////////////// Formteachers Annual Results Summary ////////////////////////////////////////////
# get Students Student Annual Results Summary for a session
@api_view(['POST'])
def getAnnualResultSummaries(request):
    data = request.data
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    classsubjectsallocations = Subjectallocation.objects.get(classname=student_class,school=school)
    studentAnnualResultSummary = []
    for student in studentsinclass:
        student_dict = {
            'Name': student.student_name,
        }
        for subject in classsubjectsallocations.subjects.all():
            subject_results = {}
            for term in ['1st', '2nd', '3rd','Total', "Ave"]:  # Assuming terms are fixed
                try:
                    subresult = AnnualSubjectResult.objects.get(Student_name=student, subject=subject, AcademicSession=session, Term=term)
                    if term == '1st':
                        subject_results[term] = subresult.FirstTermTotal
                    elif term == '2nd':
                        subject_results[term] = subresult.SecondTermTotal
                    elif term == '3rd':
                        subject_results[term] = subresult.ThirdTermTotal
                    elif term == 'Total':
                        subject_results[term] = subresult.Total
                    elif term == 'Ave':
                        subject_results[term] = subresult.Average
                except AnnualSubjectResult.DoesNotExist:
                    subject_results[term] = "-"
            student_dict[subject.subject_code] = subject_results
        studentAnnualResultSummary.append(student_dict)
    studentAnnualResultSummaryjson = json.dumps(studentAnnualResultSummary)
    return Response(studentAnnualResultSummaryjson)


# post Students Student Annual Results Summary for a session
@api_view(['POST'])
def postAnnualResultSummaries(request):
    data = request.data
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    for student in studentsinclass:
        studentresult,created = AnnualResultSummary.objects.get_or_create(Student_name=student,AcademicSession=session)
        studentresult.TotalScore = data['TotalScore']
        studentresult.Totalnumber = data['Totalnumber']
        studentresult.Average = data['Average']
        studentresult.Position = data['Position']
        studentresult.PrincipalVerdict = data['PrincipalVerdict']
        studentresult.save()
    return Response('Annual Class Results Published Successfully, and now open for viewing')