# Luizalabs project - Employee Manager

## Configuration

- Clone git repository

```
git clone https://github.com/brunochikuji/luizalabs_project.git
```
- Create the virtualenv

- Install the requirements
```
pip3 install -r requirements.txt
OR
pip install -r requirements.txt
```

- Run tests
```
pytest
```

- execute this commands
```
python3 manage.py migrate
python3 manage.py runserver
```


### Endpoints

##### Admin interface
```
url: /admin
username: luizalabs
password: luizalabs
```

#### API
##### Employees
```
url: /employee/
GET: Return list of employees
POST: Create a new employee
```
##### Employee
```
url: /employee/<employee_id>
GET: Return an employee
DELETE: Delete an employee
```

##### Department
```
url: /department/
GET: Return all departments
```
