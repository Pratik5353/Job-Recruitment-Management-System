from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [("candidate", "Candidate"), ("recruiter", "Recruiter")]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="candidate")
    phone = models.CharField(max_length=30, blank=True)
    headline = models.CharField(max_length=180, blank=True)
    location = models.CharField(max_length=120, blank=True)
    company = models.CharField(max_length=180, blank=True)

    def __str__(self):
        return f"{self.get_full_name() or self.username} ({self.role})"
