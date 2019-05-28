"""Employee view"""
from rest_framework import viewsets

from core.models import Employee
from core.serializers.employee import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """Employee view"""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
