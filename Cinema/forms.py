from django import forms


class DiscountForm(forms.Form):
    type = forms.CharField()
    amount = forms.IntegerField()
    description = forms.TextInput()
    active = forms.BooleanField()


DiscountFormSet = forms.formset_factory(DiscountForm)
