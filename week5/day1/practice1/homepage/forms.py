from django import forms

from .models import Coffee

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ('name', 'price', 'drink_kind', 'stock')
        labels = {
            'name' : '제품명',
            'price' : '가격',
            'drink_kind' : '음료 종류',
            'stock' : '재고량',
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.TextInput(attrs={'class':'form-control'}),
            'drink_kind' : forms.TextInput(attrs={'class':'form-control'}),
            'stock' : forms.TextInput(attrs={'class':'form-control'}),
        }