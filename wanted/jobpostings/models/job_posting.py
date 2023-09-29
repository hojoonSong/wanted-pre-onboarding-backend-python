from django.db import models
from .company import Company


class JobPosting(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    reward = models.IntegerField()
    content = models.TextField()
    technology = models.CharField(max_length=255)
