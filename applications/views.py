from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from jobs.models import Job
from .forms import ApplicationForm, ApplicationStatusForm
from .models import Application

@login_required
def apply_job(request, job_id):
    if request.user.role != "candidate":
        messages.error(request, "Only candidates can apply for jobs.")
        return redirect("job_detail", pk=job_id)
    job = get_object_or_404(Job, pk=job_id, is_active=True)
    if Application.objects.filter(candidate=request.user, job=job).exists():
        messages.info(request, "You already applied for this job.")
        return redirect("job_detail", pk=job.pk)
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.candidate = request.user
            application.job = job
            application.save()
            try:
                from .tasks import send_application_confirmation
                send_application_confirmation.delay(application.pk)
            except Exception:
                pass
            messages.success(request, "Application submitted successfully.")
            return redirect("dashboard")
    else:
        form = ApplicationForm()
    return render(request, "applications/apply.html", {"form": form, "job": job})

@login_required
def application_list(request):
    if request.user.role == "recruiter":
        applications = Application.objects.filter(job__created_by=request.user).select_related("candidate", "job")
    else:
        applications = Application.objects.filter(candidate=request.user).select_related("job")
    return render(request, "applications/application_list.html", {"applications": applications})

@login_required
def update_application(request, pk):
    application = get_object_or_404(Application, pk=pk, job__created_by=request.user)
    if request.method == "POST":
        form = ApplicationStatusForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, "Application status updated.")
            return redirect("application_list")
    else:
        form = ApplicationStatusForm(instance=application)
    return render(request, "applications/update.html", {"form": form, "application": application})
