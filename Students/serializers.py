from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
from utils import *

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    studentclass = serializers.SerializerMethodField()
    student_school = serializers.SerializerMethodField()
    headshot = serializers.SerializerMethodField()
    headshot_url = serializers.SerializerMethodField()
    headshot_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Student
        exclude = ['student_class','student_pin']

    def get_user(self, obj):
        return {"id":obj.user.id,"username":obj.user.username}
    
    def get_studentclass(self, obj):
        return {"id":obj.student_class.id,"class_":obj.student_class.Class}
    
    def get_student_school(self, obj):
        return {"id":obj.student_school.id,"school":obj.student_school.Schoolname}
    
    def get_headshot_url(self, obj):
        return get_full_image_url(obj.headshot)
    
    def get_headshot_name(self, obj):
        return get_image_name(obj.headshot)