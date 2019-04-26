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
]
