from django.db import models
from .job_posting import JobPosting


class Applicant(models.Model):
    user_id = models.IntegerField(unique=True)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
