from django.test import TestCase
from rest_framework.exceptions import ValidationError  # 임포트 추가
from wanted.jobpostings.dao.applicant_repository import ApplicantRepository
from wanted.jobpostings.models import Company, JobPosting
from wanted.jobpostings.services.applicant_service import ApplicantService


class ApplicantServiceTest(TestCase):

    def setUp(self):
        self.repository = ApplicantRepository()
        self.service = ApplicantService(self.repository)

        self.company = Company.objects.create(name="TestCo", country="TestLand", region="TestRegion")
        self.job_posting1 = JobPosting.objects.create(
            company=self.company, position="Backend Developer", reward=20000, content="Backend Developer Job",
            technology="Django"
        )
        self.job_posting2 = JobPosting.objects.create(
            company=self.company, position="Frontend Developer", reward=15000, content="Frontend Developer Job",
            technology="React"
        )

    def test_apply_to_job(self):
        application = self.service.apply_to_job(1, self.job_posting1.id)
        self.assertEqual(application.user_id, 1)
        self.assertEqual(application.job_posting_id, self.job_posting1.id)

        with self.assertRaises(ValidationError):
            self.service.apply_to_job(1, self.job_posting1.id)

        application = self.service.apply_to_job(1, self.job_posting2.id)
        self.assertEqual(application.user_id, 1)
        self.assertEqual(application.job_posting_id, self.job_posting2.id)
