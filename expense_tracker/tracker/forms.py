from django import forms
from .models import Expense, Category

class ExpenseForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select Category")

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
