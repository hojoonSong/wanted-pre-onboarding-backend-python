class ApplicantService:
    def __init__(self, applicant_repository):
        self.applicant_repository = applicant_repository

    def get_all_applicants(self):
        return self.applicant_repository.get_all_applicants()

    def get_applicant_by_id(self, user_id):
        return self.applicant_repository.get_applicant_by_id(user_id)