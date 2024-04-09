from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    studentclass = serializers.SerializerMethodField()
    student_school = serializers.SerializerMethodField()
    class Meta:
        model = Student
        exclude = ['student_class']

    def get_studentclass(self, obj):
        return {"id":obj.student_class.id,"class_":obj.student_class.Class}
    
    def get_student_school(self, obj):
        return {"id":obj.student_school.id,"school":obj.student_school.Schoolname}