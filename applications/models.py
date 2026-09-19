from django.conf import settings
from django.db import models
from jobs.models import Job

class Application(models.Model):
    STATUS = [
        ("applied", "Applied"), ("screening", "Screening"),
        ("shortlisted", "Shortlisted"), ("interview", "Interview"),
        ("offered", "Offered"), ("rejected", "Rejected"), ("withdrawn", "Withdrawn")
    ]
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="applications")
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="applied")
    recruiter_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(fields=["candidate", "job"], name="unique_candidate_job")
        ]

    def __str__(self):
        return f"{self.candidate} → {self.job}"
