from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Application
from .serializers import ApplicationSerializer
from .permissions import ApplicationPermission
from jobs.models import Job

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, ApplicationPermission]
    search_fields = ["job__title", "job__company", "candidate__email"]
    filterset_fields = ["status"]

    def get_queryset(self):
        user = self.request.user
        if user.role == "recruiter":
            return Application.objects.filter(job__created_by=user).select_related("candidate", "job")
        return Application.objects.filter(candidate=user).select_related("job")

    def create(self, request, *args, **kwargs):
        job_id = request.data.get("job")
        job = Job.objects.filter(pk=job_id, is_active=True).first()
        if not job:
            return Response({"detail": "Active job not found."}, status=status.HTTP_404_NOT_FOUND)
        if Application.objects.filter(candidate=request.user, job=job).exists():
            return Response({"detail": "You already applied to this job."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(candidate=request.user, job=job)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
