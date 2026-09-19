from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import JobViewSet
from .views import job_list, job_detail, job_create

router = DefaultRouter()
router.register("jobs", JobViewSet, basename="job")

urlpatterns = [
    path("jobs/", job_list, name="job_list"),
    path("jobs/new/", job_create, name="job_create"),
    path("jobs/<int:pk>/", job_detail, name="job_detail"),
    path("api/", include(router.urls)),
]
