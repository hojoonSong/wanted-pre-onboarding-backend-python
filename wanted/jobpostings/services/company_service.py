class CompanyService:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def get_all_companies(self):
        return self.company_repository.get_all_companies()

    def get_company_by_id(self, company_id):
        return self.company_repository.get_company_by_id(company_id)