from ..models.company import Company


class CompanyRepository:
    def get_all_companies(self):
        return Company.objects.all()

    def get_company_by_id(self, company_id):
        return Company.objects.get(id=company_id)
