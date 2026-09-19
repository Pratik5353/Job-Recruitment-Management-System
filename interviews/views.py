from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from applications.models import Application
from .forms import InterviewForm

@login_required
def schedule_interview(request, application_id):
    if request.user.role != "recruiter":
        messages.error(request, "Only recruiters can schedule interviews.")
        return redirect("dashboard")
    application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    if request.method == "POST":
        form = InterviewForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.application = application
            interview.interviewer = request.user
            interview.save()
            application.status = "interview"
            application.save(update_fields=["status", "updated_at"])
            messages.success(request, "Interview scheduled.")
            return redirect("application_list")
    else:
        form = InterviewForm()
    return render(request, "interviews/schedule.html", {"form": form, "application": application})
