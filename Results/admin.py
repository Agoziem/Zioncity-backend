from django.contrib import admin
from .models import ResultSummary,SubjectResult,AnnualResultSummary,AnnualSubjectResult

admin.site.register(ResultSummary)
admin.site.register(SubjectResult)
admin.site.register(AnnualResultSummary)
admin.site.register(AnnualSubjectResult)


# @admin.register(Student_Result_Data)
# # class Student_Result_DataAdmin(admin.ModelAdmin):
# #     list_display = ('Student_name', 'Position', 'display_Class', 'Average')
# #     ordering = ('Student_name', 'Position', 'Average')
# #     search_fields = ('Student_name__student_class','Position', 'Average')
# #     list_filter = ('Student_name__student_class','Student_name', 'Position', 'Average')

# #     def display_Class(self, obj):
# #         return obj.Student_name.student_class

# #     display_Class.short_description = 'Class'