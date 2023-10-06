from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import JobPosting
from ..serializers.job_posting import (JobPostingSerializer,
                                       JobPostingCreateSerializer,
                                       JobPostingDetailSerializer,
                                       JobPostingDetailWithContentSerializer)
from ..services.job_posting_service import JobPostingService
from ..dao.job_posting_repository import JobPostingRepository


class JobPostingViewSet(mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer
    job_posting_service = JobPostingService(JobPostingRepository())

    def get_serializer_class(self):
        if self.action in ['create']:
            return JobPostingCreateSerializer
        elif self.action == 'job_posting_detail':
            return JobPostingDetailWithContentSerializer
        elif self.action == 'list':
            return JobPostingDetailSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            job_posting = self.job_posting_service.create_job_posting(serializer.validated_data)
            return Response(JobPostingSerializer(job_posting).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            job_posting = self.job_posting_service.update_job_posting(instance.id, serializer.validated_data)
            return Response(JobPostingSerializer(job_posting).data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.job_posting_service.delete_job_posting(instance.id)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', '')
        queryset = self.job_posting_service.list_and_search(search)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def job_posting_detail(self, request, pk=None):
        job_posting, other_postings = self.job_posting_service.get_job_posting_detail(pk)
        serialized_data = JobPostingDetailWithContentSerializer(job_posting).data
        return Response(serialized_data, status=status.HTTP_200_OK)
