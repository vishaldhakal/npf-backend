from django.contrib import admin
from .models import DonationContent
from django import forms
from tinymce.widgets import TinyMCE
from unfold.admin import ModelAdmin


# Use TinyMCE for the content field
class DonationContentForm(forms.ModelForm):
    class Meta:
        model = DonationContent
        fields = "__all__"
        widgets = {
            "content": TinyMCE(),
        }


