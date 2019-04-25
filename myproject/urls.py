from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.views.generic.base import TemplateView


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^admin/', admin.site.urls),
    url('^employee_portal/', include('employee_portal.urls')),
]
