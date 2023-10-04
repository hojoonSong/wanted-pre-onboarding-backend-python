class JobPostingService:
    def __init__(self, job_posting_repository):
        self.job_posting_repository = job_posting_repository

    def create_job_posting(self, data):
        return self.job_posting_repository.create_job_posting(data)

    def update_job_posting(self, job_posting_id, validated_data):
        job_posting = self.job_posting_repository.get(job_posting_id)

        for field, value in validated_data.items():
            if field != 'company_id':
                setattr(job_posting, field, value)

        job_posting.save()

        return job_posting

    def delete_job_posting(self, job_posting_id):
        job_posting = self.job_posting_repository.get(job_posting_id)
        self.job_posting_repository.delete(job_posting)

    def list_and_search(self, search=''):
        return self.job_posting_repository.list_and_search(search)

    def get_job_posting_detail(self, job_posting_id):
        job_posting = self.job_posting_repository.get_detail(job_posting_id)
        other_postings = self.job_posting_repository.get_other_postings_by_company(job_posting.company.id, job_posting.id)
        return job_posting, other_postings








