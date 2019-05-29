"""Employee view"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import Employee, Department
from core.serializers.employee import EmployeeSerializer


class EmployeeViewSet(APIView):
    """Employee view"""

    @classmethod
    def get(cls, request, employee_id=None):
        """Get all employees"""
        try:
            if employee_id:
                employee = Employee.objects.get(id=int(employee_id))
                employee_serializer = EmployeeSerializer(employee)
            else:
                employees = Employee.objects.all()
                employee_serializer = EmployeeSerializer(employees, many=True)
            return Response(employee_serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(cls._get_response_error('Error on get employees', error),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def post(cls, request):
        """Create a new employee"""
        try:
            params = request.POST
            cls._valid_employee_params(params)
            department = Department.objects.get(id=params['department_id'])
            if not department:
                raise Exception('Department not found', 404)
            employee = Employee.objects.create(
                name=params['name'].strip(), email=params['email'], department=department)

            return Response({'id': employee.id}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response(cls._get_response_error('Error on delete employees', error),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @classmethod
    def delete(cls, request, employee_id=None):
        """Delete a employee"""
        try:
            if not employee_id:
                raise Exception('Bad request', 400)
            employee = Employee.objects.get(id=employee_id)
            if not employee:
                raise Exception('Employee not found', 404)
            employee.delete()

            return Response({'id': employee.id}, status=status.HTTP_204_NO_CONTENT)

        except Exception as error:
            return Response(cls._get_response_error('Error on delete employees', error),
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @staticmethod
    def _get_response_error(error_message, error_details):
        """
        Return error
        :param str error_message: Error message
        :param Exception error_details: Error details
        :return dict: Error in dict format
        """
        return {
            'message': error_message,
            'details': error_details
        }

    @staticmethod
    def _valid_employee_params(params):
        """
        Valid employee params
        :param dict params: Request params
        """
        params_required = ['name', 'email', 'department_id']
        for param_required in params_required:
            if not params.get(param_required):
                raise Exception('Bad request', 400)
