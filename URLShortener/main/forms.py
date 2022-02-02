from django import forms
from .models import Main

class NewLinkForm(forms.ModelForm):
    url = forms.CharField(max_length=200)
    class Meta:
        model = Main
        fields = ['url']
