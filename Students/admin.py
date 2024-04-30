from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('firstname','surname','student_id','student_class')
    ordering=('student_class','firstname')
    search_fields=('firstname','surname','student_id','student_class')
    list_filter=('student_class',"firstname",'surname','student_id')

