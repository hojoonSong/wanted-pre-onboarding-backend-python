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



