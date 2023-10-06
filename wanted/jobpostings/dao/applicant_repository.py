from ..models import JobPosting, Applicant


class ApplicantRepository:
    @staticmethod
    def create_application(data):
        job_posting = JobPosting.objects.get(id=data["job_posting_id"])
        return Applicant.objects.create(user_id=data["user_id"], job_posting=job_posting)

    @staticmethod
    def check_if_already_applied(user_id, job_posting_id):
        return Applicant.objects.filter(user_id=user_id, job_posting_id=job_posting_id).exists()

