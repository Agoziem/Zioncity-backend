from django.contrib import admin
from .models import ResultSummary,SubjectResult,AnnualResultSummary,AnnualSubjectResult

admin.site.register(ResultSummary)
admin.site.register(SubjectResult)
admin.site.register(AnnualResultSummary)
admin.site.register(AnnualSubjectResult)