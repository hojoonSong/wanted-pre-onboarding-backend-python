from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import JobPosting
from ..serializers.job_posting import JobPostingSerializer, JobPostingCreateSerializer
from ..services.job_posting_service import JobPostingService
from ..dao.job_posting_repository import JobPostingRepository


class JobPostingViewSet(mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    job_posting_service = JobPostingService(JobPostingRepository())

    def create(self, request, *args, **kwargs):
        serializer = JobPostingCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            job_posting = self.job_posting_service.create_job_posting(serializer.validated_data)
            return Response(JobPostingSerializer(job_posting).data, status=status.HTTP_201_CREATED)

    def update_job_posting(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = JobPostingCreateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            job_posting = self.job_posting_service.update_job_posting(instance.id, serializer.validated_data)
            return Response(JobPostingSerializer(job_posting).data, status=status.HTTP_200_OK)
