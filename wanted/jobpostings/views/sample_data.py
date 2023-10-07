from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from ..models import User
from ..serializers import CompanySerializer


class SampleCompanyView(CreateAPIView):
    serializer_class = CompanySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SampleUserView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        user = User.objects.create()
        return Response({'id': user.id}, status=status.HTTP_201_CREATED)