from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User
from utils import *

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    student_school = serializers.SerializerMethodField()
    headshot = serializers.ImageField(allow_null=True, required=False)
    headshot_url = serializers.SerializerMethodField()
    headshot_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        exclude = ['student_pin']

    def get_user(self, obj):
        return {"id":obj.user.id,"username":obj.user.username}
    
    def get_student_school(self, obj):
        return {"id":obj.student_school.id,"school":obj.student_school.Schoolname}
    
    def get_headshot_url(self, obj):
        return get_full_image_url(obj.headshot)
    
    def get_headshot_name(self, obj):
        return get_image_name(obj.headshot)