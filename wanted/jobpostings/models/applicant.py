from django.db import models
from .job_posting import JobPosting


class Applicant(models.Model):
    user_id = models.IntegerField()
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user_id', 'job_posting']
