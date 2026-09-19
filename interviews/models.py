from django.conf import settings
from django.db import models
from applications.models import Application

class Interview(models.Model):
    TYPES = [("video", "Video"), ("phone", "Phone"), ("onsite", "On-site")]
    STATUS = [("scheduled", "Scheduled"), ("completed", "Completed"), ("cancelled", "Cancelled")]
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name="interviews")
    interviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="interviews_conducted")
    scheduled_at = models.DateTimeField()
    interview_type = models.CharField(max_length=20, choices=TYPES, default="video")
    meeting_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default="scheduled")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["scheduled_at"]

    def __str__(self):
        return f"{self.application} — {self.scheduled_at}"
