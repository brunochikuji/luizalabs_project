"""Test Employee View"""
import pytest
import json
from core.models import Employee, Department


@pytest.mark.django_db
@pytest.mark.urls('luizalabs_project.urls')
def test_get_employees(client):
    """Test get employees"""
    department_development = Department.objects.create(name='Development')
    department_tech_recruiter = Department.objects.create(name='Tech Recruiter')
    first_employee = Employee.objects.create(
        name='Bruno', email='bruno.chikuji@luizalabs.com', department=department_development)
    second_employee = Employee.objects.create(
        name='Riane Silva', email='riane.silva@luizalabs.com', department=department_tech_recruiter)

    response = json.loads(client.get('/employee/').content)
    assert len(response) == 2

    assert response[0] == {
        'id': first_employee.id, 'name': 'Bruno', 'email': 'bruno.chikuji@luizalabs.com', 'department': 'Development'}
    assert response[1] == {
        'id': second_employee.id, 'name': 'Riane Silva',
        'email': 'riane.silva@luizalabs.com', 'department': 'Tech Recruiter'}


@pytest.mark.django_db
@pytest.mark.urls('luizalabs_project.urls')
def test_get_employee(client):
    """Test get employee"""
    department_development = Department.objects.create(name='Development')
    employee = Employee.objects.create(
        name='Bruno', email='bruno.chikuji@luizalabs.com', department=department_development)
    response = json.loads(client.get('/employee/{0}/'.format(employee.id)).content)
    assert response == {
        'id': employee.id,
        'name': 'Bruno',
        'email': 'bruno.chikuji@luizalabs.com',
        'department': 'Development'
    }


@pytest.mark.django_db
@pytest.mark.urls('luizalabs_project.urls')
def test_create_employee(client):
    """Test create employee"""
    department = Department.objects.create(name='Development')
    params = {
        'name': 'Bruno Chikuji',
        'email': 'bruno-chikuji@hotmail.com',
        'department_id': department.id
    }
    response = json.loads(client.post('/employee/', params).content)
    assert response == {'id': 1}


@pytest.mark.django_db
@pytest.mark.urls('luizalabs_project.urls')
def test_delete_employee(client):
    """Test delete employee"""
    employee = Employee.objects.create(
        name='Bruno', email='bruno.chikuji@luizalabs.com', department=Department.objects.create(name='Development'))
    response = client.delete('/employee/{0}/'.format(employee.id))

    assert response.status_code == 204
