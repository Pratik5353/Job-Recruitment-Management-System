from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import ResumeViewSet
from .views import resume_upload, resume_list

router = DefaultRouter()
router.register("resumes", ResumeViewSet, basename="resume")

urlpatterns = [
    path("resumes/", resume_list, name="resume_list"),
    path("resumes/upload/", resume_upload, name="resume_upload"),
    path("api/", include(router.urls)),
]
