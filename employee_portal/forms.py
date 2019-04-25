from django import forms
from models import *
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = employees
        widgets = {
        'password': forms.PasswordInput(),
    }
