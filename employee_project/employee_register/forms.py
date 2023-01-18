from django import forms
from .models import Employee

class Employe_Form(forms.ModelForm):
    class Meta:
        model=Employee
        fields=('fullname','emp_code','mobile','position')
    def __init__(self, *args, **kwargs):
        super(Employe_Form,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        self.fields['emp_code'].required =False
