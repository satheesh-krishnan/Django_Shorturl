from django import forms

class urlforms(forms.Form):
    urlform=forms.CharField(widget=forms.TextInput(attrs={'size':50}))
