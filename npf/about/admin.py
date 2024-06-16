from django.contrib import admin
from .models import (
    FAQ,
    Testimonial,
    OurTeam,
    OurClient,
    Image,
    Video,
    Donation,
)
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE
from django import forms

# Register your models here.


class OurTeamForm(forms.ModelForm):
    class Meta:
        model = OurTeam
        fields = "__all__"
        widgets = {
            "bio": TinyMCE(),
        }


class OurTeamAdmin(ModelAdmin):
    form = OurTeamForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "role",
                    "name",
                    "photo",
                    "bio",
                    "facebook",
                    "instagram",
                    "linkedin",
                    "twitter",
                    "hierarchy_level",
                )
            },
        ),
    )


admin.site.register(OurTeam, OurTeamAdmin)
admin.site.register(FAQ, ModelAdmin)
admin.site.register(Testimonial, ModelAdmin)
admin.site.register(OurClient, ModelAdmin)
admin.site.register(Image, ModelAdmin)
admin.site.register(Video, ModelAdmin)
admin.site.register(Donation, ModelAdmin)
