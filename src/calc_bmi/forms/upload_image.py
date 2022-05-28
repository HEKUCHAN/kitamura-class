from turtle import width
from django import forms


class UploadImageForm(forms.Form):
    target = forms.ImageField(required=True)

