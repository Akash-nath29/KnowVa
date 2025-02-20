from django import forms
from .models import Material

class MaterialUploadForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["title", "file", "description"]
