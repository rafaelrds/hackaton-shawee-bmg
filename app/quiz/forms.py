from django import forms

class ExpensesForm(forms.Form):
    income = forms.DecimalField(label='Ganhos', min_value=0, max_digits=10, decimal_places=2)
    expenses = forms.DecimalField(label='Gastos', min_value=0, max_digits=10, decimal_places=2)
