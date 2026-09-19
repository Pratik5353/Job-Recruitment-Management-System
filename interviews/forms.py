from django import forms
from .models import Interview

class InterviewForm(forms.ModelForm):
    scheduled_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=["%Y-%m-%dT%H:%M"]
    )
    class Meta:
        model = Interview
        fields = ("scheduled_at", "interview_type", "meeting_link", "notes", "status")
