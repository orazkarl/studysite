from django import forms

from .models import Template1


class Template1Form(forms.ModelForm):
    class Meta:
        model = Template1
        exclude = ['template1_status',]
        # fields = '__all__'

