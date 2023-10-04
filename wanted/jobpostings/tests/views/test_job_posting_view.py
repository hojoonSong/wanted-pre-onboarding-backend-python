from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from wanted.jobpostings.models import Company, JobPosting


class JobPostingViewSetTest(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(name="TestCo", country="TestLand", region="TestRegion")
        self.url = reverse('job-posting-list')

        # 기본 생성 데이터
        self.create_data = {
            "company_id": self.company.id,
            "position": "Backend Developer",
            "reward": 20000,
            "content": "We are hiring a backend developer.",
            "technology": "Django"
        }

    def test_create_job_posting(self):
        response = self.client.post(self.url, self.create_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPosting.objects.count(), 1)
        self.assertEqual(JobPosting.objects.first().position, "Backend Developer")

    def test_update_job_posting(self):
        # 먼저 JobPosting 객체를 생성
        job_posting = JobPosting.objects.create(
            company=self.company,
            position="Frontend Developer",
            reward=18000,
            content="We are hiring a frontend developer.",
            technology="React"
        )

        # 업데이트 할 데이터
        update_data = {
            "position": "Fullstack Developer",
            "technology": "Django + React"
        }

        update_url = reverse('job-posting-detail', args=[job_posting.id])

        response = self.client.patch(update_url, update_data, format='json')

        job_posting.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(job_posting.position, "Fullstack Developer")
        self.assertEqual(job_posting.technology, "Django + React")

    def test_delete_job_posting(self):
        company = Company.objects.create(name="TestCo", country="TestLand", region="TestRegion")

        # JobPosting 객체를 생성
        job_posting = JobPosting.objects.create(
            company=company,
            position="Frontend Developer",
            reward=18000,
            content="We are hiring a frontend developer.",
            technology="React"
        )

        url = reverse('job-posting-detail', args=[job_posting.id])

        # 채용공고를 삭제합니다.
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPosting.objects.count(), 0)

