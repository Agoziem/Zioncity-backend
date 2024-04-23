from rest_framework import serializers
from .models import ResultSummary,SubjectResult,AnnualResultSummary,AnnualSubjectResult

class ResultSummarySerializer(serializers.ModelSerializer):
    Student_name = serializers.SerializerMethodField()
    Term = serializers.SerializerMethodField()
    AcademicSession = serializers.SerializerMethodField()
    class Meta:
        model = ResultSummary
        fields = '__all__'
    
    def get_Student_name(self, obj):
        return {'firstname': obj.Student_name.firstname, 'surname': obj.Student_name.surname}
    

    def get_Term(self, obj):
        return {"id":obj.Term.id, 'term': obj.Term.term}
    
    def get_AcademicSession(self, obj):
        return {"id":obj.AcademicSession.id, 'session': obj.AcademicSession.session}
    


class SubjectResultSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()
    Subject = serializers.SerializerMethodField()
    Term = serializers.SerializerMethodField()
    AcademicSession = serializers.SerializerMethodField()
    student_class = serializers.SerializerMethodField()
    student_school = serializers.SerializerMethodField()
    class Meta:
        model = SubjectResult
        fields = '__all__'

    def get_student(self, obj):
        return obj.student.firstname
    
    def get_Subject(self, obj):
        return obj.Subject.subject_name
    
    def get_Term(self, obj):
        return obj.Term.term
    
    def get_AcademicSession(self, obj):
        return obj.AcademicSession.session
    
    def get_student_class(self, obj):
        return obj.student_class.Class
    
    def get_student_school(self, obj):
        return obj.student_school.Schoolname

class AnnualResultSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualResultSummary
        fields = '__all__'

class AnnualSubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualSubjectResult
        fields = '__all__'
        