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



def registrarloginpage(request):
    template = loader.get_template('emp/registrar.html')
    context={}
    return HttpResponse(template.render(context,request))

#iamregistrar
def register_login(request):
    print("lolwa")
    if request.method == 'POST':
        reg_username=request.POST['reg_username']
        reg_password=request.POST['reg_password']
        if reg_username is not None:
            if reg_special.objects.filter(username = reg_username).exists():
                reg_special_obj = reg_special.objects.get(username = reg_username)
                if reg_special_obj is None:
                    context = {'error_message': 'Invalid login'}
                    template = loader.get_template('emp/registrar.html')
                    return HttpResponse(template.render(context, request))
                elif reg_special_obj is not None:
                    if reg_special_obj.password == reg_password:
                        return redirect('/employee_portal/registrar_home')
                    else:
                        context = {'error_message': 'Invalid login'}
                        template = loader.get_template('emp/registrar.html')
                        return HttpResponse(template.render(context, request))
                else:
                    context = {'error_message': 'Invalid login'}
                    template = loader.get_template('emp/registrar.html')
                    return HttpResponse(template.render(context, request))
            else:
                context = {'error_message': 'Invalid login'}
                template = loader.get_template('emp/registrar.html')
                return HttpResponse(template.render(context, request))
    return redirect('/registrar_home/')


def send_payment_form(request):
    context={}
    template = loader.get_template('emp/send_payment_form.html')
    return HttpResponse(template.render(context, request))



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


def registrar_home(request):
        template = loader.get_template('emp/registrar_home.html')
        context={}
        return HttpResponse(template.render(context,request))



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



def pay_slip_form(request):
    if request.session.has_key('employee_id'):
        employee_id=request.session['employee_id']
        context={}
        template = loader.get_template('emp/pay_slip_form.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('/employee_portal/')


def pay_slip_request(request):
    template = loader.get_template('emp/payslip.html')
    if request.session.has_key('employee_id'):
        employee_id = request.session['employee_id']
        if request.method=="GET":
            Month = request.GET['Month']
            if not Month:
                context = {
                    'error_message': 'Month cannot be empty'
                }
                return redirect('/employee_portal/pay_slip_form')

            employee_obj=employees.objects.get(employee_id=employee_id)
            pay_slip_obj=pay_slip.objects.get(employee_id=employee_obj.employee_id, month_and_year=Month)

            total=pay_slip_obj.total
            pay=pay_slip_obj.pay
            bonus=pay_slip_obj.bonus


            # if pay_slip_obj is None:
            #     context = {
            #         'error_message': 'Pay slip not found'
            #     }
            #     return redirect('/employee_portal/pay_slip_form')
            context={
            'pay_slip_obj':pay_slip_obj
            }
        return HttpResponse(template.render(context,request))
    else:
        return redirect('/employee_portal/')

def payment_request(request):
    template = loader.get_template('emp/registrar_home.html')
    if request.method=="POST":
        year_month=request.POST['year_month']
        pay=request.POST['pay']
        bonus=request.POST['bonus']
        id=request.POST['id']
        total=int(pay)+int(bonus)
        employee_obj = employees.objects.get(employee_id = id)
        cfti_matrix_obj = cfti_matrix.objects.get(pay=pay)
        print("uqEHFBEIRVGIWUHFAvujfbpIUHfan[I9QEPOBUFU9pwGVBED[IUVESF]]")
        print(employee_obj)
        if not year_month:
            context = {
                'error_message': 'year and month cannot be empty'
            }
            return redirect('/employee_portal/send_payment_form')
        if not pay:
            context = {
                'error_message': 'pay cannot be empty'
            }
            return redirect('/employee_portal/send_payment_form')
        if not id:
            context = {
                'error_message': 'employee_id cannot be empty'
            }
            return redirect('/employee_portal/send_payment_form')

        # pay_slip_instance = pay_slip.objects.create(employee_id=employee_obj.employee_id, month_and_year=year_month, pay=pay, bonus=bonus, total=total)
        pay_slip_instance = pay_slip()
        pay_slip_instance.employee_id = employee_obj
        pay_slip_instance.year_month=year_month
        pay_slip_instance.pay=cfti_matrix_obj
        pay_slip_instance.bonus=bonus
        pay_slip_instance.total=total
        pay_slip_instance.save()
    context={}
    return HttpResponse(template.render(context,request))
