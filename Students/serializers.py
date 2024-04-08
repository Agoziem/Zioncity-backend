from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'student_name', 'Sex', 'student_class','student_id','student_pin','student_Photo','student_school')