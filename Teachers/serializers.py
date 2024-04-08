from rest_framework import serializers
from .models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'firstName', 'lastName', 'phone_number', 'email', 'teachers_id', 'role', 'subjects_taught',
                  'classes_taught', 'classFormed', 'school', 'headshot')