from rest_framework.exceptions import ValidationError
from ..models import JobPosting


class ApplicantService:
    def __init__(self, applicant_repository):
        self.applicant_repository = applicant_repository

    def apply_to_job(self, user_id, job_posting_id):
        if self.applicant_repository.check_if_already_applied(user_id, job_posting_id):
            raise ValidationError("User already applied for this job")
        return self.applicant_repository.create_application({"user_id": user_id, "job_posting_id": job_posting_id})

