from django import forms
from Basic_App.models import Checkout


class Checkoutform(forms.ModelForm):

    class Meta:
        model=Checkout
        fields=[
        'fname',
        'lname',
        'c_name',
        'email',
        'states',
        'address',
        'town',
        'zipcode',
        'phone_number',
        'comment',
        ]
