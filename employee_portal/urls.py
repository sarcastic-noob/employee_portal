from . import views
from django.conf.urls import url


app_name = 'employee_portal'

urlpatterns = [
	url('^$', views.index, name='index'),
	url('^login/$', views.login_user, name='login'),
	url('^home/$', views.home, name='home'),
	url('^logout/$', views.logout_user, name='logout'),
	url('^leave_request_form/$', views.leave_request_form, name='leave_request_form'),
	url('^submit_leave_request/$', views.submit_leave_request, name='submit_leave_request'),
	url('^pay_slip_form/$', views.pay_slip_form, name='pay_slip_form'),
	url('^pay_slip_request/$', views.pay_slip_request, name='pay_slip_request')

]
