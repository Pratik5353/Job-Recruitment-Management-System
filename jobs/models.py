from django.conf import settings
from django.db import models

class Job(models.Model):
    WORK_TYPES = [("remote", "Remote"), ("hybrid", "Hybrid"), ("onsite", "On-site")]
    EMPLOYMENT_TYPES = [("full_time", "Full-time"), ("part_time", "Part-time"), ("contract", "Contract")]
    EXPERIENCE_CHOICES = [
        ("0-1", "0–1 years"), ("1-3", "1–3 years"), ("2-4", "2–4 years"),
        ("3-5", "3–5 years"), ("5+", "5+ years")
    ]

    title = models.CharField(max_length=180)
    company = models.CharField(max_length=180)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    location = models.CharField(max_length=120, default="Remote")
    work_type = models.CharField(max_length=20, choices=WORK_TYPES, default="remote")
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES, default="full_time")
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default="1-3")
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    skills = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="jobs")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["is_active", "-created_at"]),
            models.Index(fields=["work_type", "employment_type"]),
        ]

    def __str__(self):
        return f"{self.title} — {self.company}"
