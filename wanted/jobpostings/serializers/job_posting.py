from rest_framework import serializers
from ..models import JobPosting, Company


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ('id', 'company_id', 'position', 'reward', 'content', 'technology')


class JobPostingCreateSerializer(serializers.ModelSerializer):
    company_id = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(), source='company')

    class Meta:
        model = JobPosting
        fields = ('company_id', 'position', 'reward', 'content', 'technology')

    def create(self, validated_data):
        return JobPosting.objects.create(**validated_data)


class JobPostingDetailSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.name')
    company_country = serializers.CharField(source='company.country')
    company_region = serializers.CharField(source='company.region')

    class Meta:
        model = JobPosting
        fields = ('id', 'company_name', 'company_country', 'company_region', 'position', 'reward', 'content', 'technology')