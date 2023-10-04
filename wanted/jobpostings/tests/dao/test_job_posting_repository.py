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

    def test_list_and_search(self):
        JobPosting.objects.create(**self.job_posting_data)

        # Search without a Keyword
        results = self.repository.list_and_search()
        self.assertEqual(len(results), 1)

        # Search with a Keyword
        results = self.repository.list_and_search(search="TestCo")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].company.name, "TestCo")

    def test_get_detail(self):
        job_posting = JobPosting.objects.create(company=self.company, position="Backend Developer", reward=20000)
        fetched_job_posting = self.repository.get_detail(job_posting.id)
        self.assertEqual(fetched_job_posting.position, "Backend Developer")

    def test_get_other_postings_by_company(self):
        job_posting1 = JobPosting.objects.create(company=self.company, position="Backend Developer", reward=20000)
        job_posting2 = JobPosting.objects.create(company=self.company, position="Frontend Developer", reward=20000)
        other_postings = self.repository.get_other_postings_by_company(self.company.id, job_posting1.id)
        self.assertEqual(len(other_postings), 1)
        self.assertEqual(other_postings.first().position, "Frontend Developer")



