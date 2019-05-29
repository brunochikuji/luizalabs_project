"""Department view"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Department
from core.serializers.department import DepartmentSerializer


class DepartmentViewSet(APIView):
    """Department view class"""

    @staticmethod
    def get(response):
        """Get all departments"""
        try:
            departments_query = Department.objects.all()
            departments_serializer = DepartmentSerializer(departments_query, many=True)

            return Response(departments_serializer.data, status=status.HTTP_200_OK)

        except Exception as error:
            return Response(
                {
                    'message': 'Error on get departments',
                    'details': str(error)
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )