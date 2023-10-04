from ..models.job_posting import JobPosting
from django.shortcuts import get_object_or_404
from django.db.models import Q


class JobPostingRepository:
    def get(self, job_posting_id):
        return get_object_or_404(JobPosting, id=job_posting_id)

    def create_job_posting(self, data):
        return JobPosting.objects.create(**data)

    def delete(self, job_posting):
        job_posting.delete()

    def list_and_search(self, search=''):
        queryset = JobPosting.objects.all()
        if search:
            queryset = queryset.filter(Q(company__name__icontains=search) | Q(technology__icontains=search))
        return queryset
