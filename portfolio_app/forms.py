from django.forms import ModelForm
from django import forms
from .models import ContactMessage


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full bg-gray-800 text-white border border-gray-600 rounded px-3 py-2"
            }),
            "email": forms.EmailInput(attrs={
                "class": "w-full bg-gray-800 text-white border border-gray-600 rounded px-3 py-2"
            }),
            "message": forms.Textarea(attrs={
                "class": "w-full bg-gray-800 text-white border border-gray-600 rounded px-3 py-2 h-32"
            }),
        }
