from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wanted.jobpostings.views.job_posting import JobPostingViewSet

router = DefaultRouter()
router.register(r'job-postings', JobPostingViewSet, basename='job-posting')

urlpatterns = [
    path('api/', include(router.urls)),
]
