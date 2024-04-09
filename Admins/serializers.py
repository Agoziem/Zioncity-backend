from rest_framework import serializers
from .models import *


# serializers for the models in the Admins app
class AdminSerializer(serializers.ModelSerializer):
    school = serializers.SerializerMethodField()
    class Meta:
        model = Administrator
        fields = '__all__'

    def get_school(self, obj):
        return {'id': obj.school.id, 'name': obj.school.Schoolname}

# serializer for the school model
class SchoolSerializer(serializers.ModelSerializer):
    sessions = serializers.SerializerMethodField()
    classes = serializers.SerializerMethodField()
    subjects = serializers.SerializerMethodField()
    class Meta:
        model = School
        exclude = ['session', 'Subjects']


    def get_sessions(self, obj):
        session_data = obj.session.all()
        return [{"id":session.id,"session":session.session} for session in session_data]
    
    def get_classes(self, obj):
        classes_data = obj.classes.all()
        return [{"id":class_.id,"class":class_.Class} for class_ in classes_data]
    
    def get_subjects(self, obj):
        subjects_data = obj.Subjects.all()
        return [{"id":subject.id,"subject":subject.subject_name} for subject in subjects_data]


# serializer for the academic session model
class AcademicSessionSerializer(serializers.ModelSerializer):
    terms = serializers.SerializerMethodField()
    class Meta:
        model = AcademicSession
        fields = '__all__'
    
    def get_terms(self, obj):
        terms_data = obj.terms.all()
        return [{"id":term.id,"term":term.term} for term in terms_data]

# serializer for the term model
class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

# serializer for the class model
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

# serializer for the subject model
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

# serializer for the subject allocation model
class SubjectallocationSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()
    classname = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    class Meta:
        model = Subjectallocation
        fields = '__all__' 

    
    def get_subjects(self, obj):
        subjects_data = obj.subjects.all()
        return [{"id":subject.id,"name":subject.subject_name} for subject in subjects_data]

    def get_classname(self, obj):
        return{'id': obj.classname.id, 'name': obj.classname.Class}
    
    def get_school(self, obj):
        return {'id': obj.school.id, 'name': obj.school.Schoolname}

    