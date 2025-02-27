from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
import re


class Author(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField(blank=True)
    quotes = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/")
    verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    rating_number = models.FloatField(default=0.0)
    total_reviews = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_thumbnail = models.ImageField(upload_to="category_thumbnails/")
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BaseContent(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=1000)
    title = models.CharField(max_length=1000)
    is_featured = models.BooleanField(default=False)
    hero = models.ImageField(upload_to="heroes/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    cover = models.ImageField(upload_to="covers/")
    duration = models.CharField(max_length=20)
    description = models.TextField(max_length=2000)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views_count = models.PositiveIntegerField(default=0)  # New field

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Blog(BaseContent):
    pass


class Publication(BaseContent):
    pdf = models.FileField(upload_to="pdfs/", blank=True, null=True)


class Event(BaseContent):
    location = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField(max_length=2000, null=True, blank=True)
    pdf = models.FileField(upload_to="pdfs/", blank=True, null=True)


class OpportunityType(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=1000)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000, null=True, blank=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subcategories",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def has_subcategories(self):
        return self.subcategories.exists()

    def get_subcategories(self):
        return self.subcategories.all()

    def clean(self):
        if self.parent and self.parent == self:
            raise ValidationError("A category cannot be its own parent.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Opportunity(BaseContent):
    category = models.ForeignKey(
        OpportunityType, on_delete=models.CASCADE, related_name="opportunities"
    )
    subcategory = models.ForeignKey(
        OpportunityType,
        null=True,
        blank=True,
        related_name="opportunities_as_subcategory",
        on_delete=models.CASCADE,
    )
    description = models.TextField(max_length=2000, null=True, blank=True)
    pdf = models.FileField(upload_to="pdfs/")


class Skills(models.Model):
    name = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Jobs(models.Model):
    title = models.CharField(max_length=2000)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=1000)
    description = models.TextField(max_length=2000, null=True, blank=True)
    location = models.CharField(max_length=2000)
    salary = models.CharField(max_length=2000)
    type = models.CharField(max_length=2000)
    experience = models.CharField(max_length=2000)
    level = models.CharField(max_length=2000)
    skills = models.ManyToManyField(Skills)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to="covers/")
    deadline = models.DateField()
    description = models.TextField(max_length=2000)
    content = models.TextField()
    published = models.BooleanField(default=True)
    urgent = models.BooleanField(default=False)

    def __str__(self):
        return self.title


def custom_slugify(text: str) -> str:
    if not text:
        return ""
    
    # Convert English to lowercase, leave Nepali as is
    text = re.sub(r'[a-zA-Z]+', lambda m: m.group(0).lower(), text)
    
    # Remove special characters but keep Nepali, English letters, and numbers
    text = re.sub(r'[^\u0900-\u097F\w\s-]', '', text)
    
    # Replace spaces and multiple hyphens with single hyphen
    text = re.sub(r'[-\s]+', '-', text.strip())
    
    return text


@receiver(pre_save, sender=Blog)
@receiver(pre_save, sender=Publication)
@receiver(pre_save, sender=Event)
@receiver(pre_save, sender=Opportunity)
@receiver(pre_save, sender=OpportunityType)
@receiver(pre_save, sender=Jobs)
def update_slug(sender, instance, **kwargs):
    if not instance.pk:  # This is a new instance
        instance.slug = custom_slugify(instance.title)
    elif (
        not instance.slug or instance.title != sender.objects.get(pk=instance.pk).title
    ):
        instance.slug = custom_slugify(instance.title)

    # Remove this line to prevent infinite recursion
    # instance.save()
