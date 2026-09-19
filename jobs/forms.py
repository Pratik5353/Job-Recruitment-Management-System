from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = (
            "title", "company", "description", "requirements", "location",
            "work_type", "employment_type", "experience", "salary_min",
            "salary_max", "skills", "is_active"
        )
        widgets = {
            "description": forms.Textarea(attrs={"rows": 7}),
            "requirements": forms.Textarea(attrs={"rows": 6}),
            "skills": forms.TextInput(attrs={"placeholder": "Python, Django, DRF, PostgreSQL"}),
        }
