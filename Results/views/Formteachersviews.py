from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import *
from ..models import *
from Admins.models import *
from Students.models import Student

# //////////////////////////////////////////// Formteachers Results Summary ////////////////////////////////////////////

# get all student results total for a term 
@api_view(['POST'])
def getResultSummaries(request):
    data = request.data
    print(data)
    term = Term.objects.get(id=data['term_id'])
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    studentsinclass = Student.objects.filter(student_class=student_class, student_school=school)
    totalnumber = len(studentsinclass)
    try:
        classsubjectsallocations = Subjectallocation.objects.get(classname=student_class, school=school)
        studentResultSummary = []
        for student in studentsinclass:
            resultsummary, created = ResultSummary.objects.get_or_create(Student_name=student, Term=term,
                                                                         AcademicSession=session)
            student_dict = {
                'id': resultsummary.id,
                'firstname': student.firstname,
                'surname': student.surname,
                'middlename': student.othername,
                'TotalScore': resultsummary.TotalScore,
                'Totalnumber': totalnumber,
                'Average': resultsummary.Average,
                'Position': resultsummary.Position,
                'Remark': resultsummary.Remark,
                'published': resultsummary.published
            }

            # List to store subjects total scores for the student
            subjects_total = []

            for subject in classsubjectsallocations.subjects.all():
                try:
                    subresult = SubjectResult.objects.get(student=student, student_class=student_class,
                                                           Subject=subject, Term=term, AcademicSession=session)
                    # Append subject total score to the subjects_total list
                    subjects_total.append({
                        'subject_code': subject.subject_code,
                        'subject_name': subject.subject_name,
                        'subject_total': subresult.Total,
                        'published': subresult.published
                    })
                except SubjectResult.DoesNotExist:
                    subjects_total.append({
                        'subject_code': subject.subject_code,
                        'subject_name': subject.subject_name,
                        'subject_total': '-',
                        'published': False
                    })

            # Add subjects_total list to the student dictionary
            student_dict['subjects_total'] = subjects_total

            studentResultSummary.append(student_dict)

        return Response(studentResultSummary)
    except Subjectallocation.DoesNotExist:
        return Response('No Subjects Allocated to this Class yet', status=status.HTTP_404_NOT_FOUND)


# post all student results summary for a term
@api_view(['POST'])
def postResultSummaries(request):
    data = request.data
    for studentsummary in data:
        try:
            studentresult = ResultSummary.objects.get(id=studentsummary['id'])
            fields_to_update = ['TotalScore','Totalnumber','Average',
                                    'Position','Remark']
            for field in fields_to_update:
                if field in studentsummary:
                    setattr(studentresult, field, studentsummary[field])
            studentresult.published = True
            studentresult.save()
        except Exception as e:
            print(str(e))
            pass
    return Response('Class Results Published Successfully, and now open to student for viewing')


# unpublish all student results summary for a term
@api_view(['PUT'])
def unpublishResultSummaries(request):
    data = request.data
    for studentsummary in data:
        try:
            studentresult = ResultSummary.objects.get(id=studentsummary['id'])
            studentresult.published = False
            studentresult.save()
        except Exception as e:
            print(str(e))
            pass
    return Response('Class Results Unpublished Successfully, and now closed to student for viewing')


# //////////////////////////////////////////// Formteachers Annual Results ////////////////////////////////////////////

# get Students Student Annual Results Summary for a session
@api_view(['POST'])
def getAnnualResultSummaries(request):
    data = request.data
    session = AcademicSession.objects.get(id=data['session_id'])
    school = School.objects.get(id=data['school_id'])
    student_class = Class.objects.get(id=data['class_id'])
    studentsinclass = Student.objects.filter(student_class=student_class,student_school=school)
    totalnumberinclass = len(studentsinclass)
    classsubjectsallocations = Subjectallocation.objects.get(classname=student_class,school=school)
    studentAnnualResultSummary = []
    try:
        for student in studentsinclass:
            studentannualsummary,created = AnnualResultSummary.objects.get_or_create(Student_name=student,AcademicSession=session)
            student_dict = {
                'id': studentannualsummary.id,
                'firstname': student.firstname,
                'surname': student.surname,
                'middlename': student.othername,
                'subjects':[],
                'TotalScore': studentannualsummary.TotalScore,
                'Totalnumber': totalnumberinclass,
                'Average': studentannualsummary.Average,
                'Position': studentannualsummary.Position,
                'PrincipalVerdict': studentannualsummary.PrincipalVerdict
            }
            for subject in classsubjectsallocations.subjects.all():
                subject_results = {}
                for term in ['1st', '2nd', '3rd','Total', "Ave",'published']:  # Assuming terms are fixed
                    try:
                        subresult = AnnualSubjectResult.objects.get_or_create(student=student, Subject=subject, AcademicSession=session)
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
                        elif term == 'published':
                            subject_results[term] = subresult.published
                    except Exception as e:
                        print(str(e))
                        continue
                student_dict['subjects'].append({subject.subject_code: subject_results})
            studentAnnualResultSummary.append(student_dict)
        return Response(studentAnnualResultSummary)
    except Exception as e:
        print(str(e))
        return Response(studentAnnualResultSummary)


# post Students Student Annual Results Summary for a session
@api_view(['PUT'])
def postAnnualResultSummaries(request):
    data = request.data
    for student in data:
        try:
            studentresult = AnnualResultSummary.objects.get(id=student['id'])
            fields_to_update = ['TotalScore','Totalnumber','Average','Position','PrincipalVerdict']
            for field in fields_to_update:
                if field in student:
                    setattr(studentresult, field, student[field])
            studentresult.published = True
            studentresult.save()
        except Exception as e:
            print(str(e))
            pass
    return Response('Annual Class Results Published Successfully, and now open for viewing')

@api_view(['POST'])
def unpublishAnnualResultSummaries(request):
    data = request.data
    for student in data:
        try:
            studentresult = AnnualResultSummary.objects.get(id=student['id'])
            studentresult.published = False
            studentresult.save()
        except Exception as e:
            print(str(e))
            pass
    return Response('Annual Class Results Unpublished Successfully, and now closed for viewing')