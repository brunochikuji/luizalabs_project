"""Department serializer"""
from rest_framework import serializers

from core.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    """Department serializer"""

    class Meta:
        model = Department
        fields = ('id', 'name')
