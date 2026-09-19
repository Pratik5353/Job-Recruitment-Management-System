from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.core.validators import FileExtensionValidator

class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[migrations.CreateModel(
        name="Resume",
        fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("title",models.CharField(default="My Resume",max_length=120)),
            ("file",models.FileField(upload_to="resumes/%Y/%m/",validators=[FileExtensionValidator(["pdf","doc","docx"])])),
            ("is_primary",models.BooleanField(default=True)),
            ("uploaded_at",models.DateTimeField(auto_now_add=True)),
            ("candidate",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="resumes",to=settings.AUTH_USER_MODEL)),
        ],
        options={"ordering":["-uploaded_at"]},
    )]
