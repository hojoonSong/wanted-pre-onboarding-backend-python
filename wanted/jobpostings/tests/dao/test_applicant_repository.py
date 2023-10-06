from django.test import TestCase
from wanted.jobpostings.models import Applicant, JobPosting, Company
from wanted.jobpostings.dao.applicant_repository import ApplicantRepository


class ApplicantRepositoryTest(TestCase):

    def setUp(self):
        self.repository = ApplicantRepository()
        self.company = Company.objects.create(name="TestCo", country="TestLand", region="TestRegion")
        self.job_posting = JobPosting.objects.create(
            company=self.company, position="Backend Developer", reward=20000, content="Backend Developer Job", technology="Django"
        )
        self.applicant_data = {
            "user_id": 1,
            "job_posting_id": self.job_posting.id
        }

    def test_create_application(self):
        applicant = self.repository.create_application(self.applicant_data)
        self.assertEqual(applicant.user_id, 1)

    def test_check_if_already_applied(self):
        Applicant.objects.create(**self.applicant_data)
        self.assertTrue(self.repository.check_if_already_applied(1, self.job_posting.id))
        self.assertFalse(self.repository.check_if_already_applied(2, self.job_posting.id))