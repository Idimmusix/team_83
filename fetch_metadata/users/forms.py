
from django import forms
from .models import user_Upload

class user_Upload_Form(forms.ModelForm):
    class Meta:
        model = user_Upload
        fields = ['author', 'title', 'file',]