from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('fname', 'lname', 'age', 'gender', 'address', 'eemail')
        labels = {
            'fname': 'First Name',
            'lname': 'Last Name',
            'age': 'Age',
            'gender': 'Gender',
            'address': 'Address',
            'eemail': 'E-mail',
        }
