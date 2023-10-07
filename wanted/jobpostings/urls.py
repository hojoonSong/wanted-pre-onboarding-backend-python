# wanted/jobpostings/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wanted.jobpostings.views.job_posting import JobPostingViewSet
from wanted.jobpostings.views.applicant import ApplicantViewSet
from wanted.jobpostings.views.sample_data import SampleUserView, SampleCompanyView

router = DefaultRouter()
router.register(r'job-postings', JobPostingViewSet, basename='job-posting')
router.register(r'applicants', ApplicantViewSet, basename='applicant')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/sample/user/', SampleUserView.as_view(), name='sample_user'),
    path('api/sample/company/', SampleCompanyView.as_view(), name='sample_company')
]