from turtle import width
from django import forms


class CalcBmiForm(forms.Form):
    height = forms.FloatField()
    width = forms.FloatField()
