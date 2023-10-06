from rest_framework import serializers
from wanted.jobpostings.models import Applicant, JobPosting


class ApplicantSerializer(serializers.ModelSerializer):
    job_posting_id = serializers.IntegerField(write_only=True)
    job_posting = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Applicant
        fields = ('id', 'user_id', 'job_posting_id', 'job_posting')

    def to_representation(self, instance):
        return {
            'job_posting_id': instance.job_posting.id,
            'user_id': instance.user_id
        }

