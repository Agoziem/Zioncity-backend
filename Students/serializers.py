from rest_framework import serializers
from .models import Student, StudentClassEnrollment
from django.contrib.auth.models import User
from utils import *

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    student_school = serializers.SerializerMethodField()
    class_ = serializers.SerializerMethodField()
    headshot = serializers.ImageField(allow_null=True, required=False)
    headshot_url = serializers.SerializerMethodField()
    headshot_name = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['student_pin']

    def get_user(self, obj):
        return {"id":obj.user.id,"username":obj.user.username}
    
    def get_student_school(self, obj):
        return {"id":obj.student_school.id,"school":obj.student_school.Schoolname}
    

    def get_class_(self, obj):
        enrollment = StudentClassEnrollment.objects.filter(student=obj).last()
        if enrollment:
            return {
                "id": enrollment.student_class.id,
                "class_name": enrollment.student_class.Class,  # Adjust as needed
                "academic_session": enrollment.academic_session.session,  # Adjust as needed
            }
        return None 
    
    def get_headshot_url(self, obj):
        return get_full_image_url(obj.headshot)
    
    def get_headshot_name(self, obj):
        return get_image_name(obj.headshot)