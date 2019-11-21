from django import forms
from .models import login,signup

class FormName(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"

class FormSignup(forms.ModelForm):
    class Meta:
        model = signup
        fields = "__all__"
