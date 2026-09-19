from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api import InterviewViewSet
from .views import schedule_interview

router = DefaultRouter()
router.register("interviews", InterviewViewSet, basename="interview")

urlpatterns = [
    path("applications/<int:application_id>/interview/", schedule_interview, name="schedule_interview"),
    path("api/", include(router.urls)),
]
