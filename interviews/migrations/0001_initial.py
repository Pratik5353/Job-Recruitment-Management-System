from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[("applications","0001_initial"),migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[migrations.CreateModel(
        name="Interview",
        fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("scheduled_at",models.DateTimeField()),
            ("interview_type",models.CharField(choices=[("video","Video"),("phone","Phone"),("onsite","On-site")],default="video",max_length=20)),
            ("meeting_link",models.URLField(blank=True)),
            ("notes",models.TextField(blank=True)),
            ("status",models.CharField(choices=[("scheduled","Scheduled"),("completed","Completed"),("cancelled","Cancelled")],default="scheduled",max_length=20)),
            ("created_at",models.DateTimeField(auto_now_add=True)),
            ("application",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="interviews",to="applications.application")),
            ("interviewer",models.ForeignKey(null=True,on_delete=django.db.models.deletion.SET_NULL,related_name="interviews_conducted",to=settings.AUTH_USER_MODEL)),
        ],
        options={"ordering":["scheduled_at"]},
    )]
