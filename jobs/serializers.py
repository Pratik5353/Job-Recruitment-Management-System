from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    created_by_name = serializers.CharField(source="created_by.get_full_name", read_only=True)
    salary = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = "__all__"
        read_only_fields = ("created_by", "created_at", "updated_at")

    def get_salary(self, obj):
        if obj.salary_min and obj.salary_max:
            return f"₹{obj.salary_min:,} – ₹{obj.salary_max:,}"
        return "Not disclosed"
