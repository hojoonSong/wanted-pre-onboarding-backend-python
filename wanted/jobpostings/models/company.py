from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
