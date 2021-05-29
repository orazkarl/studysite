from django import forms

from .models import Template1


class Template1Form(forms.ModelForm):
    class Meta:
        model = Template1
        # exclude = ['inspector',]
        fields = '__all__'

