from django import forms
from .models import Product

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
    def clean_price(self):
        price = self.cleaned_data['price']
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price
