import floppyforms as forms
from models import Product


class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'update_at',)

    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError('Price must be greater than zero')
        return self.cleaned_data['price']


class ProductAddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=100, widget=forms.NumberInput(attrs={'size': 2, 'value': 1, 'class': 'quantity'}))
    product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data
