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
	url('^view_comments/$', views.view_comments, name='view_comments'),
	url('^approve', views.approve, name='approve'),
	url('^decline', views.decline, name='decline'),
	url('^add_comments', views.add_comments, name='add_comments'),
	url('^submit_comment', views.submit_comment, name='submit_comment'),
	url('^pay_slip_form/$', views.pay_slip_form, name='pay_slip_form'),
	url('^pay_slip_request/$', views.pay_slip_request, name='pay_slip_request'),
	url('^registrarloginpage/$',views.registrarloginpage,name='registrarloginpage'),
	url('^register_login/$',views.register_login,name='register_login'),
	url('^registrar_home/$',views.registrar_home,name='registrar_home'),
	url('^send_payment_form/$',views.send_payment_form,name='send_payment_form'),
	url('^payment_request/$',views.payment_request,name='payment_request'),

]
