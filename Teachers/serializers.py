from rest_framework import serializers
from .models import Teacher
from django.contrib.auth.models import User
from utils import * 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password', 'email', 'first_name', 'last_name')

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    classes_taught = serializers.SerializerMethodField()
    subjects_taught = serializers.SerializerMethodField()
    school = serializers.SerializerMethodField()
    classFormed = serializers.SerializerMethodField()
    headshot = serializers.ImageField(allow_null=True, required=False)
    headshot_url = serializers.SerializerMethodField()
    headshot_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = '__all__'
        
    def get_user(self, obj):
        return {"id":obj.user.id,"username":obj.user.username}
    
    def get_classes_taught(self, obj):
        return [{'id': class_taught.id, 'name': class_taught.Class} for class_taught in obj.classes_taught.all()]
    
    def get_subjects_taught(self, obj):
        return [{'id': subject_taught.id, 'name': subject_taught.subject_name} for subject_taught in obj.subjects_taught.all()]
    
    def get_school(self, obj):
        return {'id': obj.school.id, 'name': obj.school.Schoolname}
    
    def get_classFormed(self, obj):
        if obj.classFormed is not None:
            return {'id': obj.classFormed.id, 'name': obj.classFormed.Class}
        else:
            return None
    
    def get_headshot_url(self, obj):
        return get_full_image_url(obj.headshot)
    
    def get_headshot_name(self, obj):
        return get_image_name(obj.headshot)



    
