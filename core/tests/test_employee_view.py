"""Test Employee View"""
import pytest
import json
from core.models import Employee, Department


@pytest.mark.django_db
@pytest.mark.urls('luizalabs_project.urls')
def test_get_employee(client):
    """Test get employee"""
    department_development = Department.objects.create(name='Development')
    department_tech_recruiter = Department.objects.create(name='Tech Recruiter')
    Employee.objects.create(name='Bruno', email='bruno.chikuji@luizalabs.com', department=department_development)
    Employee.objects.create(name='Riane Silva', email='riane.silva@luizalabs.com', department=department_tech_recruiter)

    response = json.loads(client.get('/employee/').content)
    assert len(response) == 2

    assert response[0] == {'name': 'Bruno', 'email': 'bruno.chikuji@luizalabs.com', 'department': 'Development'}
    assert response[1] == {'name': 'Riane Silva', 'email': 'riane.silva@luizalabs.com', 'department': 'Tech Recruiter'}
