from django.test import TestCase
from django.contrib.auth import get_user_model
from jobs.models import Job

class JobModelTests(TestCase):
    def test_job_creation(self):
        user = get_user_model().objects.create_user(
            username="r", email="r@example.com", password="pass12345", role="recruiter"
        )
        job = Job.objects.create(
            title="Python Developer",
            company="Test Co",
            description="Build APIs",
            created_by=user,
        )
        self.assertEqual(str(job), "Python Developer — Test Co")
