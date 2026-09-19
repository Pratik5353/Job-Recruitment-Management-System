from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.db import models

class Resume(models.Model):
    candidate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resumes")
    title = models.CharField(max_length=120, default="My Resume")
    file = models.FileField(upload_to="resumes/%Y/%m/", validators=[FileExtensionValidator(["pdf", "doc", "docx"])])
    is_primary = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return f"{self.candidate} — {self.title}"
