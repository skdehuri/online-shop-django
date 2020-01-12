from django import forms
from products.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if 'hello' in title:
            return
        else:
            raise forms.ValidationError('This is not a valid title')
