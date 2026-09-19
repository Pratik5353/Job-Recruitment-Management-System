from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Job
from .serializers import JobSerializer
from .permissions import IsRecruiterOrReadOnly

class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [IsRecruiterOrReadOnly]
    search_fields = ["title", "company", "description", "skills", "location"]
    filterset_fields = ["work_type", "employment_type", "experience", "is_active"]
    ordering_fields = ["created_at", "salary_min", "salary_max"]

    def get_queryset(self):
        return Job.objects.filter(is_active=True) if self.action in ("list", "retrieve") else Job.objects.all()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
