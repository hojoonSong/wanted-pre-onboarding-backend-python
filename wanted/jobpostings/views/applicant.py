from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from ..models import Applicant
from ..serializers.applicant import ApplicantSerializer
from ..services.applicant_service import ApplicantService
from ..dao.applicant_repository import ApplicantRepository


class ApplicantViewSet(viewsets.GenericViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializer
    applicant_service = ApplicantService(ApplicantRepository())

    def create(self, request, *args, **kwargs):
        serializer = ApplicantSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                application = self.applicant_service.apply_to_job(
                    serializer.validated_data['user_id'],
                    serializer.validated_data['job_posting_id']
                )
                return Response(ApplicantSerializer(application).data, status=status.HTTP_201_CREATED)
            except ValidationError as ve:
                return Response({'error': ve.detail}, status=status.HTTP_400_BAD_REQUEST)




