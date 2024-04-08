from rest_framework import serializers
from .models import ResultSummary,SubjectResult,AnnualResultSummary,AnnualSubjectResult

class ResultSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultSummary
        fields = '__all__'

class SubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectResult
        fields = '__all__'

class AnnualResultSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualResultSummary
        fields = '__all__'

class AnnualSubjectResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnnualSubjectResult
        fields = '__all__'
        