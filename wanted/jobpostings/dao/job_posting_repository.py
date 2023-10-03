from ..models.job_posting import JobPosting
from django.shortcuts import get_object_or_404


class JobPostingRepository:
    def get(self, job_posting_id):
        return get_object_or_404(JobPosting, id=job_posting_id)

    def create_job_posting(self, data):
        return JobPosting.objects.create(**data)
