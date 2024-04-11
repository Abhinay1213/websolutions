# forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'business_name', 'business_type', 'business_address')
        
class YourForm(forms.Form):
    your_field = forms.CharField(max_length=100)

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['product', 'customer_name', 'customer_email', 'message']


class ProductForm(forms.ModelForm):
    document_file = forms.FileField(required=False)

    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'company_established', 'software_name',
                  'company_website', 'software_type', 'location_countries', 'location_cities',
                  'contact_telephone', 'address', 'num_employees', 'internal_services', 'last_demo_date',
                  'last_review_date', 'business_areas', 'modules', 'client_types', 'cloud_type',
                  'additional_information']
