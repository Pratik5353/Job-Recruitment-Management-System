from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import JobForm
from .models import Job

def job_list(request):
    qs = Job.objects.filter(is_active=True)
    q = request.GET.get("q", "").strip()
    work_type = request.GET.get("work_type", "")
    experience = request.GET.get("experience", "")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(company__icontains=q) | Q(skills__icontains=q) | Q(location__icontains=q))
    if work_type:
        qs = qs.filter(work_type=work_type)
    if experience:
        qs = qs.filter(experience=experience)
    paginator = Paginator(qs, 9)
    page = paginator.get_page(request.GET.get("page"))
    return render(request, "jobs/job_list.html", {"page": page, "q": q, "work_type": work_type, "experience": experience})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, is_active=True)
    return render(request, "jobs/job_detail.html", {"job": job})

@login_required
def job_create(request):
    if request.user.role != "recruiter":
        messages.error(request, "Only recruiters can create jobs.")
        return redirect("dashboard")
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            messages.success(request, "Job published successfully.")
            return redirect("job_detail", pk=job.pk)
    else:
        form = JobForm()
    return render(request, "jobs/job_form.html", {"form": form})
