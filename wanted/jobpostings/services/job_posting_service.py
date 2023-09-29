class JobPostingService:
    def __init__(self, job_posting_repository):
        self.job_posting_repository = job_posting_repository

    def get_all_job_postings(self):
        return self.job_posting_repository.get_all_job_postings()

    def get_job_posting_by_id(self, job_posting_id):
        return self.job_posting_repository.get_job_posting_by_id(job_posting_id)