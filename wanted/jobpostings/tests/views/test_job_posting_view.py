from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from wanted.jobpostings.models import Company, JobPosting


class JobPostingViewSetTest(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(name="TestCo", country="TestLand", region="TestRegion")
        self.url = reverse('job-posting-list')

        # Base Information
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
        job_posting = JobPosting.objects.create(
            company=self.company,
            position="Frontend Developer",
            reward=18000,
            content="We are hiring a frontend developer.",
            technology="React"
        )

        # to Update
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

        # Create a Job Posting
        job_posting = JobPosting.objects.create(
            company=company,
            position="Frontend Developer",
            reward=18000,
            content="We are hiring a frontend developer.",
            technology="React"
        )

        url = reverse('job-posting-detail', args=[job_posting.id])

        # Delete this Jobposting
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobPosting.objects.count(), 0)

    def test_list_job_postings(self):
        # Add two Job Postings
        JobPosting.objects.create(**self.create_data)
        JobPosting.objects.create(
            company=self.company,
            position="Frontend Developer",
            reward=25000,
            content="We are hiring a frontend developer.",
            technology="React"
        )

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_search_job_postings(self):
        # Add two Job Postings
        JobPosting.objects.create(**self.create_data)
        JobPosting.objects.create(
            company=self.company,
            position="Frontend Developer",
            reward=25000,
            content="We are hiring a frontend developer.",
            technology="VueJS"
        )

        # Keyword with "Django"
        search_url = f"{self.url}?search=Django"
        response = self.client.get(search_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["technology"], "Django")

