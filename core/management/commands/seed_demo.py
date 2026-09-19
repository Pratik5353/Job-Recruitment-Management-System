from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from jobs.models import Job

User = get_user_model()

class Command(BaseCommand):
    help = "Create demo recruiter, candidate and sample jobs."

    def handle(self, *args, **options):
        recruiter, _ = User.objects.get_or_create(
            username="recruiter",
            defaults={"email": "recruiter@example.com", "first_name": "Aarav", "last_name": "Recruiter", "role": "recruiter", "company": "NovaTech Labs"},
        )
        recruiter.role = "recruiter"
        recruiter.email = "recruiter@example.com"
        recruiter.set_password("Recruiter@123")
        recruiter.save()

        candidate, _ = User.objects.get_or_create(
            username="candidate",
            defaults={"email": "candidate@example.com", "first_name": "Priya", "last_name": "Candidate", "role": "candidate", "location": "Ahmedabad, Gujarat"},
        )
        candidate.role = "candidate"
        candidate.email = "candidate@example.com"
        candidate.set_password("Candidate@123")
        candidate.save()

        jobs = [
            {
                "title": "Python Django Backend Developer",
                "company": "NovaTech Labs",
                "description": "Build scalable REST APIs and backend services for a modern SaaS platform.",
                "requirements": "2+ years Python/Django, REST APIs, PostgreSQL, Docker and Git.",
                "location": "Remote — India",
                "work_type": "remote",
                "employment_type": "full_time",
                "experience": "2-4",
                "salary_min": 50000,
                "salary_max": 80000,
                "skills": "Python, Django, DRF, PostgreSQL, Docker, Redis",
            },
            {
                "title": "FastAPI Backend Engineer",
                "company": "CloudForge",
                "description": "Design APIs and integrations for document processing and workflow automation.",
                "requirements": "Python, FastAPI, PostgreSQL, Docker, cloud deployment and testing.",
                "location": "Bengaluru / Remote",
                "work_type": "remote",
                "employment_type": "full_time",
                "experience": "1-3",
                "salary_min": 45000,
                "salary_max": 75000,
                "skills": "Python, FastAPI, PostgreSQL, REST, Docker, Azure",
            },
            {
                "title": "Backend Engineer — Python",
                "company": "Orbit Systems",
                "description": "Work on microservices, third-party integrations and high-quality backend APIs.",
                "requirements": "Strong Python fundamentals, OOP, REST, SQL and production debugging.",
                "location": "Ahmedabad / Hybrid",
                "work_type": "hybrid",
                "employment_type": "full_time",
                "experience": "2-4",
                "salary_min": 40000,
                "salary_max": 65000,
                "skills": "Python, Django, Microservices, PostgreSQL, Git",
            },
        ]
        for data in jobs:
            Job.objects.get_or_create(title=data["title"], company=data["company"], defaults={**data, "created_by": recruiter})
        self.stdout.write(self.style.SUCCESS("Demo data created successfully."))
