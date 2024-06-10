from django.contrib import admin
from .models import DonationContent
from django import forms
from tinymce.widgets import TinyMCE
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin


# Use TinyMCE for the content field
class DonationContentForm(forms.ModelForm):
    class Meta:
        model = DonationContent
        fields = "__all__"
        widgets = {
            "content": TinyMCE(),
        }


class CustomDonationContentAdmin(SingletonModelAdmin, ModelAdmin):
    form = DonationContentForm

    # If there are any conflicts in method resolution order, ensure SingletonModelAdmin methods are prioritized
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        SingletonModelAdmin.__init__(self, model, admin_site)


admin.site.register(DonationContent, CustomDonationContentAdmin)
