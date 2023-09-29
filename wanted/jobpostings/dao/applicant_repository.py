from ..models.applicant import Applicant


class ApplicantRepository:
    def get_all_applicants(self):
        return Applicant.objects.all()

    def get_applicant_by_id(self, user_id):
        return Applicant.objects.get(user_id=user_id)