from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    webName = forms.CharField(max_length=255, required=True)
    desc = forms.CharField(widget=forms.Textarea, required=True)
    
    urls = forms.URLField(widget=forms.TextInput(attrs={'class': 'url-input'}), required=True)
