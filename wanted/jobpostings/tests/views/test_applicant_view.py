from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from wanted.jobpostings.models import Applicant, JobPosting, Company


class ApplicantViewSetTest(APITestCase):

    def setUp(self):
        self.company = Company.objects.create(name="TestCo", country="TestLand", region="TestRegion")
        self.job_posting = JobPosting.objects.create(
            company=self.company,
            position="Backend Developer",
            reward=20000,
            content="Backend Developer Job",
            technology="Django"
        )
        self.url = reverse('applicant-list')

    def test_successful_application(self):
        response = self.client.post(self.url, {'user_id': 1, 'job_posting_id': self.job_posting.id})
        if response.status_code != status.HTTP_201_CREATED:
            print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Applicant.objects.filter(user_id=1, job_posting=self.job_posting).exists())
        self.assertEqual(response.data['user_id'], 1)
        self.assertEqual(response.data['job_posting_id'], self.job_posting.id)

    def test_duplicate_application(self):
        Applicant.objects.create(user_id=1, job_posting=self.job_posting)
        response = self.client.post(self.url, {'user_id': 1, 'job_posting_id': self.job_posting.id})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        error_message = response.data['error'][0] if isinstance(response.data['error'], list) else response.data[
            'error']
        self.assertEqual(error_message, "User already applied for this job")



