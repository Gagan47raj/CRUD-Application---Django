from django import forms
from CRUD.models import CustomerModel

class CustomerForms(forms.ModelForm):
    class Meta:

        model=CustomerModel
        fields="__all__"