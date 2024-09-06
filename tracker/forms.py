from django import forms
from .models import SubCategory

class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name', 'quantity', 'volunteer', 'comment']
