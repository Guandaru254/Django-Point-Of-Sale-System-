from django import forms

from posApp.models import Creditor, Debtors, Stock, Store

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product_name', 'quantity', 'store', 'reorder_level']

class DebtorForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = ['name','amount_owed','date_owed']

class CreditorForm(forms.ModelForm):
    class Meta:
        model = Creditor
        fields = ['name','amount','due_date']

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name','location']