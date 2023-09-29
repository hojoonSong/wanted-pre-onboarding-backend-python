from rest_framework import viewsets
from ..serializers.job_posting import JobPostingSerializer
from ..services.job_posting_service import JobPostingService
from ..dao.job_posting_repository import JobPostingRepository


class JobPostingViewSet(viewsets.ModelViewSet):
    serializer_class = JobPostingSerializer

    job_posting_service = JobPostingService(JobPostingRepository())

    def get_queryset(self):
        return self.job_posting_service.get_all_job_postings()
