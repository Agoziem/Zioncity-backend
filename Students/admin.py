from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('firstname','surname','student_id')
    ordering=('firstname',)
    search_fields=('firstname','surname','student_id')
    list_filter=("firstname",'surname','student_id')

@admin.register(StudentClassEnrollment)
class StudentClassEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'get_student_class', 'get_academic_session')
    ordering = ('student__firstname', 'student_class__Class', 'academic_session__session')
    search_fields = ('student__firstname', 'student_class__Class', 'academic_session__session')
    list_filter = ('student_class', 'academic_session')

    # Custom method to display student name
    def get_student_name(self, obj):
        return obj.student.firstname
    get_student_name.short_description = "Student Name"

    # Custom method to display class name
    def get_student_class(self, obj):
        return obj.student_class.Class
    get_student_class.short_description = "Class"

    # Custom method to display academic session
    def get_academic_session(self, obj):
        return obj.academic_session.session
    get_academic_session.short_description = "Academic Session"