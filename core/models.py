from django.db import models


class Department(models.Model):
    """Department model"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Employee model"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=None)

    def __str__(self):
        return self.name
