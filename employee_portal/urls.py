from . import views
from django.conf.urls import url


app_name = 'employee_portal'

urlpatterns = [
	url('^$', views.index, name='index'),
	url('^login/$', views.login_user, name='login'),
	url('^home/$', views.home, name='home'),

]
