from django import forms

class sms_form(forms.Form):
    name = forms.CharField(max_length=30)
    number=forms.CharField(max_length=10)
    message=forms.CharField(widget=forms.Textarea,max_length=120)