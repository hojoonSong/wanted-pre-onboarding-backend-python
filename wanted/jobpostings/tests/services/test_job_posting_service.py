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

    def test_delete_job_posting(self):
        # JobPosting 객체를 Mocking
        mock_job_posting = mock.Mock(spec=JobPosting)
        self.job_posting_repository.get.return_value = mock_job_posting

        job_posting_id = 1

        # Method 호출
        self.job_posting_service.delete_job_posting(job_posting_id)

        # 호출 검증
        self.job_posting_repository.get.assert_called_once_with(job_posting_id)
        self.job_posting_repository.delete.assert_called_once_with(mock_job_posting)

    def test_get_job_posting_detail(self):
        # JobPosting 객체와 다른 채용 정보 목록을 Mocking
        mock_job_posting = mock.Mock(spec=JobPosting, position="Backend Developer")
        mock_other_postings = []

        # repository method의 반환값을 설정
        self.job_posting_repository.get_detail.return_value = mock_job_posting
        self.job_posting_repository.get_other_postings_by_company.return_value = mock_other_postings

        job_posting_id = 1
        fetched_job_posting, other_postings = self.job_posting_service.get_job_posting_detail(job_posting_id)

        # 검증
        self.assertEqual(fetched_job_posting.position, "Backend Developer")
        self.assertEqual(len(other_postings), 0)

