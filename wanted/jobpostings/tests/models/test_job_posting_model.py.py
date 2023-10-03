from django.test import TestCase
from wanted.jobpostings.models import Company, JobPosting


class JobPostingModelTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            name="TestCo", country="TestLand", region="TestRegion"
        )

    def test_create_job_posting(self):
        job_posting = JobPosting.objects.create(
            company=self.company,
            position="Backend Developer",
            reward=20000,
            content="We are hiring a backend developer.",
            technology="Django"
        )
        self.assertEqual(job_posting.position, "Backend Developer")
