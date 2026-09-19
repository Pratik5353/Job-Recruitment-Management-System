from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from jobs.models import Job

class HomeTests(TestCase):
    def test_home_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_job_list_loads(self):
        response = self.client.get(reverse("job_list"))
        self.assertEqual(response.status_code, 200)
