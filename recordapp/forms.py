from django import forms
from . models import Patient_info, Address
from django.forms.widgets import NumberInput, Select, TextInput

class Patient_info_form(forms.ModelForm):
    hospitalNo = forms.CharField(error_messages={'required': ' Hospital Number Cannot be Empty'}, 
                                 label="Hospital No or SVC No",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Hospital/SVC Number',
                                 }),
                                  required=True)
    surname = forms.CharField(label="Surname",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Surname',
                                 }),
                                  required=True)
    othernames = forms.CharField(label="Other Names",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Other Names',
                                 }),
                                 
                                  required=True)

    data_of_birth = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    
    email = forms.EmailField(help_text='A valid email address, please.',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Email Address',
                                 }),
                                  required=False)
    phone_number = forms.CharField(
                                help_text='A valid phone number, please.',
                                label="phone number",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'phone number',
                                 }),
                                  required=False)
    occupation = forms.CharField(label="Profession",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Profession',
                                 }),
                                  required=False)
    state_of_origin = forms.CharField(label="state of origin",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'state of origin',
                                 }),
                                  required=False)
    tribe = forms.CharField(label="Trib",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Tribe',
                                 }),
                                 required=False )
    religion = forms.CharField(label="Religion",
                                 widget=forms.TextInput(attrs={'class': 'form-control', 
                                'placeholder': 'Religion',
                                 }),
                                 required=False )
    data_of_birth = forms.DateField(label="Date of Birth",
                                 widget=forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
                                 required=False )
    class Meta:
        model = Patient_info
        fields =['hospitalNo', 'surname' ,'othernames', 'data_of_birth', 'sex', 'email', 'phone_number', 'occupation', 'state_of_origin', 'tribe','religion']
        widgets = {
        'sex' : Select(attrs={'class':'form-control show-tick'}),
    }
class Patient_address_form(forms.ModelForm):
    class Meta:
        model = Address
        fields =['street_no', 'street_name', 'state', 'lga', 'city']
        