from  django import forms
import django

from django import forms
from .models import Vendor


class VendorForm(forms.Form):
     class Meta:
         model=Vendor
         field=['vendor_name','vendor_licence','vendor_licence',]