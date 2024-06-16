from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


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

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Blog(BaseContent):
    pass


class Publication(BaseContent):
    pdf = models.FileField(upload_to="pdfs/")


class Event(BaseContent):
    location = models.CharField(max_length=100)
    event_date = models.DateField()
    description = models.TextField(max_length=2000, null=True, blank=True)
    pdf = models.FileField(upload_to="pdfs/")


@receiver(post_save, sender=Blog)
@receiver(post_save, sender=Publication)
@receiver(post_save, sender=Event)
def create_slug(sender, instance, created, **kwargs):
    if created and not instance.slug:
        instance.slug = slugify(instance.title)
        instance.save()
