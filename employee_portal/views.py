from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.urls import reverse
from .models import *


# class HomepageView(TemplateView):
#     template_name = 'emp/login.html'

def index(request):
    template = loader.get_template('emp/login.html')
    context = {}
    if request.session.has_key('employee_id'):
        return home(request)
    return HttpResponse(template.render(context,request))


def login_user(request):
	if request.session.has_key('employee_id'):
		return home(request)
	if request.method == "POST":
	    employee_id = request.POST['username']
	    password = request.POST['password']
	    if employee_id is not None:
	    	if employees.objects.filter(employee_id = employee_id).exists():
	    		employee_obj = employees.objects.get(employee_id = employee_id)
		    	if employee_obj is None:
		        	context = {
		        		'error_message': 'Invalid login'
		        	}
		        	template = loader.get_template('emp/login.html')
		        	return HttpResponse(template.render(context, request))
		    	elif employee_obj is not None:
		        	if employee_obj.password == password:
		        		request.session['employee_id'] = employee_id
		        		return redirect('/employee_portal/home')
		        	else:
		        		context = {'error_message': 'Invalid login'}
		        		template = loader.get_template('emp/login.html')
		        		return HttpResponse(template.render(context, request))
		    	else:
		        	context = {
		        		'error_message': 'Invalid login'
		        	}
		        	template = loader.get_template('emp/login.html')
		        	return HttpResponse(template.render(context, request))
	    	else:
		    	context = {'error_message': 'Invalid login'}
		    	template = loader.get_template('emp/login.html')
		    	return HttpResponse(template.render(context, request))
	return redirect('/employee_portal/')


def home(request):
    if request.session.has_key('employee_id'):
        employee_id=request.session['employee_id']
        template = loader.get_template('emp/home.html')
        employee_obj = employees.objects.get(employee_id = employee_id)
        dept_id = employee_obj.dept_id
        role_id = employee_obj.role_id
        dept_obj = department.objects.get(dept_name = dept_id)
        role_obj = roles.objects.get(role_name = role_id)
        context = {'employee_obj':employee_obj, 'dept_obj': dept_obj}
        return HttpResponse(template.render(context,request))
    else:
        return redirect('/employee_portal/')


def logout_user(request):
	if request.session.has_key('employee_id'):
		del request.session['employee_id']
	return redirect('/employee_portal')
