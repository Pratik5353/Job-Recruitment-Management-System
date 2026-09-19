from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("cover_letter",)
        widgets = {
            "cover_letter": forms.Textarea(attrs={
                "rows": 7,
                "placeholder": "Tell the recruiter briefly why you are a good fit..."
            })
        }

class ApplicationStatusForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ("status", "recruiter_note")
        widgets = {"recruiter_note": forms.Textarea(attrs={"rows": 4})}
