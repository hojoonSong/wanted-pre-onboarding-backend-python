from unittest import TestCase, mock
from wanted.jobpostings.services.job_posting_service import JobPostingService
from wanted.jobpostings.models import JobPosting


class JobPostingServiceTest(TestCase):

    def setUp(self):
        self.job_posting_repository = mock.Mock()
        self.job_posting_service = JobPostingService(self.job_posting_repository)
        self.sample_data = {
            "company": mock.Mock(),
            "position": "Backend Developer",
            "reward": 20000,
            "content": "We are hiring a backend developer.",
            "technology": "Django"
        }

    def test_create_job_posting(self):
        # JobPosting 객체를 Mocking
        mock_job_posting = mock.Mock(spec=JobPosting)
        self.job_posting_repository.create_job_posting.return_value = mock_job_posting

        # Method 호출 및 검증
        job_posting = self.job_posting_service.create_job_posting(self.sample_data)
        self.job_posting_repository.create_job_posting.assert_called_once_with(self.sample_data)
        self.assertEqual(job_posting, mock_job_posting)

    def test_update_job_posting(self):
        # JobPosting 객체를 Mocking
        mock_job_posting = mock.Mock(spec=JobPosting)
        self.job_posting_repository.get.return_value = mock_job_posting

        job_posting_id = 1
        validated_data = {"position": "Updated Position"}

        # Method 호출
        updated_job_posting = self.job_posting_service.update_job_posting(job_posting_id, validated_data)

        # 호출 검증
        self.job_posting_repository.get.assert_called_once_with(job_posting_id)
        mock_job_posting.save.assert_called_once()
        self.assertEqual(mock_job_posting.position, validated_data["position"])
