from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ResumeForm
from .models import Resume

@login_required
def resume_list(request):
    resumes = Resume.objects.filter(candidate=request.user)
    return render(request, "resumes/resume_list.html", {"resumes": resumes})

@login_required
def resume_upload(request):
    if request.user.role != "candidate":
        messages.error(request, "Only candidates can upload resumes.")
        return redirect("dashboard")
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            resume = form.save(commit=False)
            resume.candidate = request.user
            resume.save()
            if resume.is_primary:
                Resume.objects.filter(candidate=request.user).exclude(pk=resume.pk).update(is_primary=False)
            messages.success(request, "Resume uploaded.")
            return redirect("resume_list")
    else:
        form = ResumeForm()
    return render(request, "resumes/resume_upload.html", {"form": form})
