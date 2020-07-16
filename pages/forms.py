from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ConsultationForm(forms.Form):
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.EmailField()
    date = forms.DateField(widget=DatePickerInput(
        format='%m/%d/%Y'), label="Preferred Date")
    description = forms.CharField(
        widget=forms.Textarea(), label="How can we help you?")
