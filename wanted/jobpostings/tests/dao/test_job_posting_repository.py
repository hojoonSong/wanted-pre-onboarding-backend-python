from django.test import TestCase
from wanted.jobpostings.dao.job_posting_repository import JobPostingRepository
from wanted.jobpostings.models import Company, JobPosting


class JobPostingRepositoryTest(TestCase):

    def setUp(self):
        self.repository = JobPostingRepository()
        self.company = Company.objects.create(
            name="TestCo", country="TestLand", region="TestRegion"
        )
        self.job_posting_data = {
            "company": self.company,
            "position": "Backend Developer",
            "reward": 20000,
            "content": "We are hiring a backend developer.",
            "technology": "Django"
        }

    def test_create_job_posting(self):
        job_posting = self.repository.create_job_posting(self.job_posting_data)
        self.assertEqual(job_posting.position, "Backend Developer")
        self.assertEqual(JobPosting.objects.count(), 1)

    def test_get_job_posting(self):
        job_posting = JobPosting.objects.create(**self.job_posting_data)
        fetched_job_posting = self.repository.get(job_posting.id)
        self.assertEqual(fetched_job_posting.position, "Backend Developer")

    def test_delete_job_posting(self):
        job_posting = JobPosting.objects.create(**self.job_posting_data)
        self.repository.delete(job_posting)
        self.assertEqual(JobPosting.objects.count(), 0)

