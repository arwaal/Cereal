from django import forms
from django.core.validators import RegexValidator
from maim.models import Cereal

# letter_val = RegexValidator(r'^[a-zA-z]*$', 'Please Type Letters')


class CerealSearch(forms.Form):
	letter_val = RegexValidator(r'^[a-zA-z]*$', 'Please Type Letters')

	name = forms.CharField(required =True, validators= [letter_val])


class CreateCereal(forms.ModelForm):
	class Meta:
		model = Cereal
		fields ='__all__'


class UserSignup(forms.Form):

	letter_val = RegexValidator(r'^[a-zA-z]*$', 'Please Type Letters')
	name = forms.CharField(required=True, validators=[letter_val])
	email = forms.CharField(required=True)
	password = forms.CharField(widget= forms.PasswordInput(), required=True)


class UserSignin(forms.Form):

	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())