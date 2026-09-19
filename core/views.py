from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from jobs.models import Job
from applications.models import Application

def home(request):
    jobs = Job.objects.filter(is_active=True).order_by("-created_at")[:6]
    return render(request, "home.html", {"jobs": jobs})

@login_required
def dashboard(request):
    if request.user.role == "recruiter":
        jobs = Job.objects.filter(created_by=request.user).order_by("-created_at")
        stats = {
            "jobs": jobs.count(),
            "applications": Application.objects.filter(job__created_by=request.user).count(),
            "shortlisted": Application.objects.filter(job__created_by=request.user, status="shortlisted").count(),
            "interviews": Application.objects.filter(job__created_by=request.user, interviews__isnull=False).distinct().count(),
        }
        return render(request, "dashboard_recruiter.html", {"jobs": jobs[:8], "stats": stats})
    applications = Application.objects.filter(candidate=request.user).select_related("job").order_by("-created_at")
    stats = {
        "applications": applications.count(),
        "shortlisted": applications.filter(status="shortlisted").count(),
        "interviews": applications.filter(interviews__isnull=False).distinct().count(),
        "offers": applications.filter(status="offered").count(),
    }
    return render(request, "dashboard_candidate.html", {"applications": applications[:8], "stats": stats})
