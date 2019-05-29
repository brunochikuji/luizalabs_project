"""Employee serializer"""
from rest_framework import serializers

from core.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer"""

    department = serializers.CharField(source='department.name', read_only=True)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')
