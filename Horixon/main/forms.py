from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'saved_amount', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'target_amount': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'saved_amount': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'deadline': forms.DateInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded', 'type': 'date'}),
        }




from .models import Budget1

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget1
        fields = ['category', 'limit', 'mounthly_in']
        widgets = {
            'category': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'limit': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
            'mounthly_in': forms.NumberInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded'}),
        }
