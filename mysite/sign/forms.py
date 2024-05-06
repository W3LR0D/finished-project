from django import forms

class textForm(forms.Form):
    name = forms.CharField(required = False, label = '', help_text = 'Please enter text for ASL translation:',
                            widget = forms.Textarea(attrs = {'rows': 2, 'cols': 40}))