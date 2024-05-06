from django.contrib import admin
from .models import *

@admin.register(Administrator)
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('admin_id','firstname','surname','role','school')
    search_fields = ('admin_id','firstname','surname','role','school')
    list_filter = ('role','school')

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('Schoolname','Schoolofficialline','Schooltype')
    search_fields = ('Schoolname','Schoolofficialline','Schooltype')
    list_filter = ('Schooltype',)

@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('session','startdate','enddate')
    search_fields = ('session','startdate','enddate')
    list_filter = ('session',)

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('term',)
    search_fields = ('term',)
    list_filter = ('term',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('Class',)
    search_fields = ('Class',)
    list_filter = ('Class',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_code','subject_name')
    search_fields = ('subject_code','subject_name')
    list_filter = ('subject_code','subject_name')

@admin.register(Subjectallocation)
class SubjectallocationAdmin(admin.ModelAdmin):
    list_display = ('school','classname')
    search_fields = ('classname',"school__Schoolname")
    list_filter = ('classname',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('Newsletterterm','Newslettersession','Newsletterdate','school')
    search_fields = ('Newsletterterm__term','Newslettersession_session','Newsletterdate','school__Schoolname')
    list_filter = ('Newsletterterm__term','Newslettersession__session','Newsletterdate','school__Schoolname')
    sortable_by = ('Newsletterterm__term','Newslettersession__session','Newsletterdate','school__Schoolname')

@admin.register(Notfication)
class NotficationAdmin(admin.ModelAdmin):
    list_display = ('headline','school','Notificationdate','is_seen')
    search_fields = ('school__Schoolname','notification','Notificationdate')
    list_filter = ('school__Schoolname','Notificationdate','is_seen')
    sortable_by = ('school__Schoolname','Notificationdate','is_seen')
