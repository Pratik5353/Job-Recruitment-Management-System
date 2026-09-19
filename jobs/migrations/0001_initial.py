from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[migrations.CreateModel(
        name="Job",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("title", models.CharField(max_length=180)),
            ("company", models.CharField(max_length=180)),
            ("description", models.TextField()),
            ("requirements", models.TextField(blank=True)),
            ("location", models.CharField(default="Remote", max_length=120)),
            ("work_type", models.CharField(choices=[("remote","Remote"),("hybrid","Hybrid"),("onsite","On-site")], default="remote", max_length=20)),
            ("employment_type", models.CharField(choices=[("full_time","Full-time"),("part_time","Part-time"),("contract","Contract")], default="full_time", max_length=20)),
            ("experience", models.CharField(choices=[("0-1","0–1 years"),("1-3","1–3 years"),("2-4","2–4 years"),("3-5","3–5 years"),("5+","5+ years")], default="1-3", max_length=20)),
            ("salary_min", models.PositiveIntegerField(blank=True, null=True)),
            ("salary_max", models.PositiveIntegerField(blank=True, null=True)),
            ("skills", models.CharField(blank=True, max_length=500)),
            ("is_active", models.BooleanField(default=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("updated_at", models.DateTimeField(auto_now=True)),
            ("created_by", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="jobs", to=settings.AUTH_USER_MODEL)),
        ],
        options={"ordering":["-created_at"]},
    ), migrations.AddIndex(model_name="job", index=models.Index(fields=["is_active","-created_at"], name="jobs_job_is_act_1c5a31_idx")),
    migrations.AddIndex(model_name="job", index=models.Index(fields=["work_type","employment_type"], name="jobs_job_work_ty_3d9a52_idx"))]
