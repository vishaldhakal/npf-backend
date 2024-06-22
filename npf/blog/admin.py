from django import forms
from django.contrib import admin
from .models import (
    Author,
    Category,
    Tag,
    Blog,
    Publication,
    Event,
    Opportunity,
    OpportunityType,
)
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE

admin.site.register(Author, ModelAdmin)
admin.site.register(Category, ModelAdmin)
admin.site.register(Tag, ModelAdmin)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widgets = {
            "content": TinyMCE(),
        }


class BlogAdmin(ModelAdmin):
    form = BlogForm
    # make slug read only
    readonly_fields = ("slug",)
    filter_horizontal = ("tags",)
    # make fields on same row
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "is_featured",
                    "hero",
                    "category",
                    "tags",
                    "cover",
                    "duration",
                    "description",
                    "content",
                    "author",
                )
            },
        ),
    )
    # title and slug on same row

    def get_queryset(self, request):
        qs = super(ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)


admin.site.register(Blog, BlogAdmin)


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = "__all__"
        widgets = {
            "content": TinyMCE(),
        }


class PublicationAdmin(ModelAdmin):
    form = PublicationForm

    readonly_fields = ("slug",)

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "is_featured",
                    "slug",
                    "hero",
                    "category",
                    "tags",
                    "cover",
                    "duration",
                    "description",
                    "content",
                    "author",
                    "pdf",
                )
            },
        ),
    )

    filter_horizontal = ("tags",)

    def get_queryset(self, request):
        qs = super(ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)


admin.site.register(Publication, PublicationAdmin)


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"
        widgets = {
            "content": TinyMCE(),
        }


class EventAdmin(ModelAdmin):
    form = EventForm

    readonly_fields = ("slug",)
    # make fields on same row
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "is_featured",
                    "slug",
                    "hero",
                    "category",
                    "tags",
                    "cover",
                    "duration",
                    "description",
                    "content",
                    "author",
                    "event_date",
                    "pdf",
                )
            },
        ),
    )

    filter_horizontal = ("tags",)

    def get_queryset(self, request):
        qs = super(ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)


admin.site.register(Event, EventAdmin)


class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = "__all__"
        widgets = {
            "content": TinyMCE(),
        }


class OpportunityAdmin(ModelAdmin):
    form = OpportunityForm

    readonly_fields = ("slug",)
    # make fields on same row
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "is_featured",
                    "slug",
                    "hero",
                    "category",
                    "tags",
                    "cover",
                    "duration",
                    "description",
                    "content",
                    "author",
                )
            },
        ),
    )

    filter_horizontal = ("tags",)

    def get_queryset(self, request):
        qs = super(ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)


admin.site.register(Opportunity, OpportunityAdmin)


class OpportunityTypeAdmin(ModelAdmin):
    readonly_fields = ("slug",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                    "parent",
                    "description",
                )
            },
        ),
    )


admin.site.register(OpportunityType, OpportunityTypeAdmin)
