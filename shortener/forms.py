from django import forms
from .models import ShortLinkModel

class ShortLinkForm(forms.ModelForm):
    class Meta:
        model = ShortLinkModel
        fields = ['origin_url']
        labels = {
            'origin_url' : '원본URL',
        }