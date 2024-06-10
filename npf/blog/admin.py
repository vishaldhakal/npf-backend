from django import forms
from django.contrib import admin
from .models import Author, SocialLinks, Category, Tag, Blog,Publication
from unfold.admin import ModelAdmin
from tinymce.widgets import TinyMCE

admin.site.register(Author, ModelAdmin)
admin.site.register(SocialLinks, ModelAdmin)
admin.site.register(Category, ModelAdmin)
admin.site.register(Tag, ModelAdmin)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }


class BlogAdmin(ModelAdmin):
    form = BlogForm
    # make slug read only
    readonly_fields = ('slug',)
    # make fields on same row
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'is_featured', 'hero', 'category', 'tags', 'cover', 'duration', 'description', 'content', 'author')
        }),
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
        fields = '__all__'
        widgets = {
            'content': TinyMCE(),
        }

class PublicationAdmin(ModelAdmin):
    form = PublicationForm
    def get_queryset(self, request):
        qs = super(ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author__user=request.user)

admin.site.register(Publication, PublicationAdmin)

