from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Interview
from .serializers import InterviewSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == "recruiter":
            return Interview.objects.filter(application__job__created_by=user)
        return Interview.objects.filter(application__candidate=user)
