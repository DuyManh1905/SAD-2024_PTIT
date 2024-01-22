from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
    def clean_price(self):
        price = self.cleaned_data['price']
        if price is not None and price <= 0:
            raise forms.ValidationError('Price must be greater than zero.')
        return price



class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(
        widget=forms.TextInput(attrs={'size': '2', 'value': '1', 'class': 'quantity', 'maxlength': '5'}),
        error_messages={'invalid': 'Please enter a valid quantity.'},
        min_value=1
    )
    product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ProductAddToCartForm, self).clean()

        if self.request:
            if not self.request.session.test_cookie_worked():
                raise ValidationError("Cookies must be enabled.")

        return cleaned_data
