from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
import re

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    studentclass = serializers.SerializerMethodField()
    student_school = serializers.SerializerMethodField()
    headshot = serializers.SerializerMethodField()
    class Meta:
        model = Student
        exclude = ['student_class','student_pin']

    def get_user(self, obj):
        return {"id":obj.user.id,"username":obj.user.username}
    
    def get_studentclass(self, obj):
        return {"id":obj.student_class.id,"class_":obj.student_class.Class}
    
    def get_student_school(self, obj):
        return {"id":obj.student_school.id,"school":obj.student_school.Schoolname}
    
    def get_headshot(self, obj):
        headshot = obj.headshot
        if not headshot:
            return None 
        headshot_url = headshot.url
        pattern_media = r'^/media/'
        pattern_percent_3A = r'%3A'
        modified_url = re.sub(pattern_media, '', headshot_url)
        modified_url = re.sub(pattern_percent_3A, ':/', modified_url, count=1)
        modified_url = re.sub(pattern_percent_3A, ':', modified_url)
        return modified_url