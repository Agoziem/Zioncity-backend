from django.contrib import admin
from .models import *


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('firstName','surname','teachers_id','role')
    ordering=('role','firstName','teachers_id')
    search_fields=('firstName','surname','teachers_id','role')
    list_filter=('role',"firstName",'surname','teachers_id')