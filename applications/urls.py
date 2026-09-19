from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import ApplicationViewSet
from .views import apply_job, application_list, update_application

router = DefaultRouter()
router.register("applications", ApplicationViewSet, basename="application")

urlpatterns = [
    path("jobs/<int:job_id>/apply/", apply_job, name="apply_job"),
    path("applications/", application_list, name="application_list"),
    path("applications/<int:pk>/status/", update_application, name="update_application"),
    path("api/", include(router.urls)),
]
