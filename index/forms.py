from django import forms
from .models import *

class donationform(forms.ModelForm):
	class Meta:
		model = donation
		fields= ('name','email','ammount','type_of_payment','message')


class Contactform(forms.ModelForm):

	class Meta:
	    
		model = Contact
		fields =('name', 'email',  'message',)
