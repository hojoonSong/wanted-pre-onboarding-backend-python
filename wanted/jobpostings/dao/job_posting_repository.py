from ..models.job_posting import JobPosting


class JobPostingRepository:
    def get_all_job_postings(self):
        return JobPosting.objects.all()

    def get_job_posting_by_id(self, job_posting_id):
        return JobPosting.objects.get(id=job_posting_id)