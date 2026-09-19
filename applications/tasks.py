from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Application

@shared_task
def send_application_confirmation(application_id):
    application = Application.objects.select_related("candidate","job").get(pk=application_id)
    if not application.candidate.email:
        return "No candidate email"
    send_mail(
        subject=f"Application received — {application.job.title}",
        message=f"Hi {application.candidate.first_name or application.candidate.username},\n\nYour application for {application.job.title} at {application.job.company} was received successfully.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[application.candidate.email],
    )
    return "sent"
