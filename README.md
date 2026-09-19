# Job Application & Recruitment Management System

A production-style Django backend + responsive web UI for managing jobs, candidates, applications, resumes and interviews.

## Stack
- Python 3.11+
- Django 5.2
- Django REST Framework
- PostgreSQL-ready (SQLite works out of the box)
- JWT authentication for API
- Django session authentication for web UI
- Celery + Redis integration
- drf-spectacular / OpenAPI
- Docker + Docker Compose
- Responsive Tailwind-style UI via CDN + custom CSS

## Features

### Candidate
- Register/login
- Browse/search/filter jobs
- View job details
- Apply to jobs
- Upload resume
- Track application status
- View interview schedule
- Candidate dashboard

### Recruiter/Admin
- Create/update/delete jobs
- View applicants
- Change application status
- Schedule interviews
- Recruiter dashboard
- Django admin

### Backend
- JWT API authentication
- Role-based permissions
- REST API
- Search/filter/pagination
- Resume upload
- PostgreSQL support
- Redis/Celery configuration
- Swagger/OpenAPI documentation
- Docker support

## Quick Start — Windows

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

copy .env.example .env

python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

Open:
- Web: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
- API docs: http://127.0.0.1:8000/api/docs/

Demo recruiter:
- Email: recruiter@example.com
- Password: Recruiter@123

Demo candidate:
- Email: candidate@example.com
- Password: Candidate@123

## Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py seed_demo
python manage.py runserver
```

## Docker

```bash
docker compose up --build
```

The Docker setup runs Django + PostgreSQL + Redis.

## Celery

Optional for local development. With Redis running:

```bash
celery -A config worker -l info
```

For periodic tasks:

```bash
celery -A config beat -l info
```

## API

### Auth
- POST `/api/auth/token/`
- POST `/api/auth/token/refresh/`

### Jobs
- GET `/api/jobs/`
- GET `/api/jobs/{id}/`
- POST `/api/jobs/` (recruiter)
- PATCH `/api/jobs/{id}/` (recruiter)

### Applications
- GET `/api/applications/`
- POST `/api/applications/`
- GET `/api/applications/{id}/`

### Resumes
- GET `/api/resumes/`
- POST `/api/resumes/`

### Interviews
- GET `/api/interviews/`
- POST `/api/interviews/`

OpenAPI:
- `/api/schema/`
- `/api/docs/`

## Important production notes
This is a portfolio-grade starter project, not a fully audited production deployment. Before real production use:
- Set `DEBUG=False`
- Set a strong `SECRET_KEY`
- Configure HTTPS and secure cookies
- Configure real email provider
- Use object storage for resumes
- Add antivirus/file scanning
- Configure allowed hosts/CORS/CSRF carefully
- Run Celery workers under a process supervisor
- Add monitoring and structured logging
