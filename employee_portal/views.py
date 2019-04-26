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

def index(request):
    template = loader.get_template('emp/login.html')
    context = {}
    if request.session.has_key('employee_id'):
        return redirect('/employee_portal/home')
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


def leave_request_form(request):
    if request.session.has_key('employee_id'):
        employee_id=request.session['employee_id']
        context={}
        template = loader.get_template('emp/leave_request_form.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/employee_portal/')

def submit_leave_request(request):
    if request.session.has_key('employee_id'):
        employee_id = request.session['employee_id']
        if request.method=="POST":
            startDate = request.POST['startDate']
            endDate = request.POST['endDate']
            reason = request.POST['reason']
            if startDate is None:
                context = {
                    'error_message': 'Start Date cannot be empty'
                }
                return redirect('/employee_portal/leave_request_form')
            if endDate is None:
                context = {
                    'error_message': 'End Date cannot be empty'
                }
                return redirect('/employee_portal/leave_request_form')
            if reason is None:
                context = {
                    'error_message': 'Reason cannot be empty'
                }
                return redirect('/employee_portal/leave_request_form')
            employee_obj=employees.objects.get(employee_id=employee_id)
            status_obj=leave_request_status.objects.get(type=employee_obj.type, stage=1)
            # curr_status=None
            # for status_obj in status_objs:
            #     if status_obj.stage==1:
            #         curr_status=status_obj
            leaveRequest = leave_request()
            leaveRequest.employee_id=employee_obj
            leaveRequest.status_id=status_obj
            leaveRequest.startDate=startDate
            leaveRequest.endDate=endDate
            leaveRequest.reason=reason
            leaveRequest.save()
            print("leave request id = " + str(leaveRequest))
            leaveRequestObj = leave_request.objects.get(request_id=leaveRequest.request_id)
            comment=comments()
            comment.request_id=leaveRequestObj
            comment.comment_by=employee_obj
            comment.comment=reason
            comment.approvalStatus="Pending"
            comment.save()

        return redirect('/employee_portal/')
    else:
        return redirect('/employee_portal/')
