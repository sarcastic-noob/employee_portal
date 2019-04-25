from __future__ import unicode_literals
from django import forms
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
# Create your models here.
now = datetime.datetime.now()


class department(models.Model):
    dept_id=models.IntegerField(primary_key=True)
    dept_name=models.CharField(max_length=25)
    dept_type=models.CharField(max_length=25)

    def __str__(self):
   	    return self.dept_name


class roles(models.Model) :
    role_id=models.IntegerField(primary_key=True)
    role_name=models.CharField(max_length=25)
    def __str__(self):
   		return self.role_name


class employees(models.Model) :
    employee_id=models.CharField(max_length=25,primary_key=True)
    name=models.CharField(max_length=40)
    dept_id=models.ForeignKey(department,on_delete=models.CASCADE)
    role_id=models.ForeignKey(roles, on_delete=models.CASCADE)
    type=models.CharField(max_length=40)
    join_date=models.DateTimeField(auto_now=True)
    leaves_this_year=models.IntegerField()
    leaves_next_year=models.IntegerField()
    password=models.CharField(max_length=50,default="abcdefgh")
    employee_email=models.CharField(max_length=100, default="")
    def __str__(self):
        return self.name



class department_roles(models.Model):
    employee_id=models.OneToOneField(employees, primary_key=True,on_delete=models.CASCADE,unique=True)
    dept_id=models.ForeignKey(department,on_delete=models.CASCADE)
    role_id=models.ForeignKey(roles,on_delete=models.CASCADE)
    start_date=models.DateTimeField(auto_now=True)
    end_date=models.DateTimeField(auto_now=True)
    def __str__(self):
   		return self.role_id



class bonus_request(models.Model):
    role_id=models.ForeignKey(roles,on_delete=models.CASCADE)
    type=models.ForeignKey(employees, on_delete=models.CASCADE)
    month_year=models.CharField(max_length=25)
    bonus=models.DecimalField(decimal_places=3,max_digits = 5)
    status=models.CharField(max_length=10)
    class Meta:
            unique_together=('role_id','month_year')


class cfti_matrix(models.Model):
    type=models.ForeignKey(employees, on_delete=models.CASCADE)
    role_id=models.ForeignKey(roles, on_delete=models.CASCADE)
    years_of_experience=models.IntegerField()
    pay=models.IntegerField()
    class Meta:
            unique_together=('type','years_of_experience')
    def __str__(self):
            return self.pay


class leave_request(models.Model):
    request_id=models.IntegerField(primary_key=True)
    employee_id=models.ForeignKey(employees,on_delete=models.CASCADE)
    status=models.CharField(max_length=10)
    comments=models.CharField(max_length=500)
    def __str__(self):
   		return self.request_id


class projects(models.Model):
    project_id=models.IntegerField(primary_key=True)
    employee_id=models.ForeignKey(employees,on_delete=models.CASCADE)
    faculty_role=models.CharField(max_length=30)
    def __str__(self):
   		return self.project_id


class project_associate(models.Model):
    project_id=models.ForeignKey(projects,on_delete=models.CASCADE)
    employee_id=models.ForeignKey(employees,on_delete=models.CASCADE)
    class Meta:
            unique_together=('project_id','employee_id')


class project_budget(models.Model):
    project_id=models.OneToOneField(projects, primary_key=True, on_delete=models.CASCADE)
    manpower_budget=models.IntegerField()
    travel_budget=models.IntegerField()
    equipment_budget=models.IntegerField()


class expenditure(models.Model):
    project_id=models.ForeignKey(projects, on_delete=models.CASCADE)
    expenditure_type=models.CharField(max_length=30)
    expenditure=models.IntegerField()


class tee_request(models.Model):
    request_id=models.IntegerField(primary_key=True)
    project_id=models.ForeignKey(projects,on_delete=models.CASCADE)
    expenditure_type=models.CharField(max_length=30)
    ammount=models.IntegerField()
    status=models.CharField(max_length=15)
    comments=models.CharField(max_length=500)


class leave_request_final(models.Model):
    request_id=models.IntegerField(primary_key=True)
    status=models.CharField(max_length=15)


class hiring_request(models.Model):
    request_id=models.IntegerField(primary_key=True)
    associate_name=models.CharField(max_length=30)
    associate_type=models.CharField(max_length=10)
    status=models.CharField(max_length=15)
    comments=models.CharField(max_length=500)
