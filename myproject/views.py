from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from employee_portal.views import *
def index(request):
	template = loader.get_template('emp/login.html')
	context = {}
	if request.session.has_key('employee_id'):
		return redirect('/employee_portal/home')

	return HttpResponse(template.render(context,request))
