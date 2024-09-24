from django.contrib import admin
from .models import DonationContent, NewsletterMember
from django import forms
from tinymce.widgets import TinyMCE
from solo.admin import SingletonModelAdmin
from unfold.admin import ModelAdmin
import csv
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _


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


class DateRangeFilter(admin.SimpleListFilter):
    title = _("Date Filter")
    parameter_name = "created_at"

    def lookups(self, request, model_admin):
        return [
            ("today", _("Today")),
            ("this_week", _("This Week")),
            ("this_month", _("This Month")),
        ]

    def queryset(self, request, queryset):
        if self.value() == "today":
            return queryset.filter(created_at__date=timezone.now().date())
        elif self.value() == "this_week":
            start_of_week = timezone.now().date() - timedelta(
                days=timezone.now().weekday()
            )
            return queryset.filter(created_at__date__gte=start_of_week)
        elif self.value() == "this_month":
            return queryset.filter(created_at__month=timezone.now().month)
        return queryset


class NewsletterMemberAdmin(ModelAdmin):
    list_display = ("email", "member_type", "created_at", "updated_at")
    list_filter = (DateRangeFilter, "member_type")
    search_fields = ("email", "name")

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = f"attachment; filename={meta}.csv"
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected as CSV"


admin.site.register(NewsletterMember, NewsletterMemberAdmin)
