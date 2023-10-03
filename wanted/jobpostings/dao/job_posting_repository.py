from ..models.job_posting import JobPosting


class JobPostingRepository:
    def create_job_posting(self, data):
        return JobPosting.objects.create(**data)