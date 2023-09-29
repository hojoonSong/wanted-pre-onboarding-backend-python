from rest_framework import serializers
from ..models import JobPosting, Company


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = ('id', 'company_id', 'position', 'reward', 'content', 'technology')
