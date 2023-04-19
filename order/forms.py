from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Chhattisgarh', 'Chhattisgarh'),
		('Rajasthan', 'Rajasthan'),
		('Delhi', 'Delhi'),
	)

	DISCRICT_CHOICES = (
		('Durg', 'Durg'), 
		('Bilaspur', 'Bilaspur'),
		('Raipur', 'Raipur'),
	)

	PAYMENT_METHOD_CHOICES = (
		('UPI', 'UPI'),
		('VISA','VISA')
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'transaction_id']
