"""Test employee"""
import pytest

from core.models import Employee, Department


@pytest.mark.django_db
class TestEmployeeModel:
    """Employee model test"""

    def test_create_employee(self):
        """test create employee"""
        department = self.create_department()
        employee = self.create_employee(department)
        assert employee == Employee.objects.get(email='bruno.chikuji@luizalabs.com')

    @staticmethod
    def create_employee(department):
        """
        Create employee for test
        :param Department department: Department
        :return Employee: Employee created for test
        """
        return Employee.objects.create(
            name='Bruno',
            email='bruno.chikuji@luizalabs.com',
            department=department
        )

    @staticmethod
    def create_department():
        """
        Create department for test
        :return Department:
        """
        return Department.objects.create(name='Development')
