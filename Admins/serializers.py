from rest_framework import serializers
from .models import *


# serializers for the models in the Admins app
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = '__all__'


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class AcademicSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSession
        fields = '__all__'


class TermSerializer(serializers.ModelSerializer):
    class Meta:
        model = Term
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class SubjectallocationSerializer(serializers.ModelSerializer):
    # subjects = serializers.SerializerMethodField()
    # classname = serializers.SerializerMethodField()
    # school = serializers.SerializerMethodField()
    class Meta:
        model = Subjectallocation
        fields = '__all__' 

    
    # def get_subjects(self, obj):
    #     subjects_data = obj.subjects.all()
    #     return [{"id":subject.id,"subject":subject.subject_name} for subject in subjects_data]

    # def get_classname(self, obj):
    #     return obj.classname.Class
    
    # def get_school(self, obj):
    #     return obj.school.Schoolname

    