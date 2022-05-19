from django import forms
from .models import Messinfo

class Messform(forms.ModelForm):
    class Meta:
        model = Messinfo
        fields = "__all__"