from django import forms
from .models import pagecontact


class regform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label='Email')
    catagary=forms.ChoiceField(choices=(('question','Question'),('other','Other'),('Only','only'),))
    sub=forms.CharField(required=False)
    body=forms.CharField(widget=forms.Textarea)



#class pagecontactForm(forms.ModelForm):
#
#     class Meta:
#         model=pagecontact
#         fields=('name','email','body')
#
