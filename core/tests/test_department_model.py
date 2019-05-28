"""Test Department model"""
import pytest

from core.models import Department


@pytest.mark.django_db
class TestDepartmentModel:
    """Department model test"""

    def test_create_department(self):
        """test create department"""
        department = self.create_department()
        assert department == Department.objects.get(name='Development')

    @staticmethod
    def create_department():
        """
        Create department for test
        :return Department:
        """
        return Department.objects.create(name='Development')
