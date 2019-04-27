from django.contrib import admin
from .models import*

admin.site.register(department)
admin.site.register(type)
admin.site.register(roles)
admin.site.register(employees)
admin.site.register(department_roles)
admin.site.register(bonus_request)
admin.site.register(cfti_matrix)
admin.site.register(leave_request)
admin.site.register(leave_request_final)
admin.site.register(projects)
admin.site.register(project_associate)
admin.site.register(project_budget)
admin.site.register(expenditure)
admin.site.register(tee_request)
admin.site.register(hiring_request)
admin.site.register(comments)
admin.site.register(leave_request_status)
admin.site.register(pay_slip)
admin.site.register(reg_special)

# Register your models here.
