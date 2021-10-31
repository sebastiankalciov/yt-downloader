from django import forms 

class URLForm(forms.Form):
    URL = forms.CharField(label = "Video URL", max_length=100)
    
