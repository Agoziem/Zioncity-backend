from django.contrib import admin
from .models import ResultSummary,SubjectResult,AnnualResultSummary,AnnualSubjectResult

@admin.register(ResultSummary)
class ResultSummaryAdmin(admin.ModelAdmin):
    list_display=('Student_name','Term','AcademicSession','published')
    ordering=('Student_name','Term')
    search_fields=('Student_name__firstname','Term__term','AcademicSession__session')
    list_filter=('Term','AcademicSession','published')

@admin.register(SubjectResult)
class SubjectResultAdmin(admin.ModelAdmin):
    list_display=('student','Subject','Term','AcademicSession','student_class','is_offering','published')
    ordering=('student','Subject','Term')
    search_fields=('student__firstname','Subject__subject_name','Term__term','AcademicSession__session','student_class__Class')
    list_filter=('Term','AcademicSession','student_class','student_school','is_offering','published')

@admin.register(AnnualResultSummary)
class AnnualResultSummaryAdmin(admin.ModelAdmin):
    list_display=('Student_name','PrincipalVerdict','AcademicSession','published')
    ordering=('Student_name','AcademicSession')
    search_fields=('Student_name__firstname','AcademicSession__session')
    list_filter=('AcademicSession','published')

@admin.register(AnnualSubjectResult)
class AnnualSubjectResultAdmin(admin.ModelAdmin):
    list_display=('student','Subject','AcademicSession','is_offering','published')
    ordering=('student','Subject','AcademicSession')
    search_fields=('student__firstname','Subject__subject_name','AcademicSession__session')
    list_filter=('AcademicSession','is_offering','published')



