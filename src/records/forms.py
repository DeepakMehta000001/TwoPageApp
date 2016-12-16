from django import forms

from .models import Record

class AddForm(forms.ModelForm):
	class Meta:
		model = Record
		fields = ['first_name','last_name','email','mobile','age','dob']