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
    avatar = models.FileField()
    verified = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    rating_number = models.FloatField(default=0.0)
    social_links = models.ForeignKey(
        "SocialLinks", on_delete=models.SET_NULL, null=True, blank=True
    )
    total_reviews = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SocialLinks(models.Model):
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.facebook


class Category(models.Model):
    name = models.CharField(max_length=100)
    category_thumbnail = models.FileField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    slug = models.SlugField(unique=True, null=True, blank=True)
    title = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)
    hero = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    cover = models.FileField()
    duration = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



@receiver(post_save, sender=Blog)
def create_blog_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

      


class Publication(models.Model):
      slug = models.SlugField(unique=True, null=True, blank=True)
      title = models.CharField(max_length=200)
      is_featured = models.BooleanField(default=False)
      hero = models.FileField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      category = models.ForeignKey(Category, on_delete=models.CASCADE)
      tags = models.ManyToManyField(Tag)
      cover = models.FileField()
      duration = models.CharField(max_length=20)
      description = models.TextField(max_length=100)
      content = models.TextField()
      author = models.ForeignKey(Author, on_delete=models.CASCADE)
      pdf = models.FileField()
      
      def __str__(self):
         return self.title


@receiver(post_save, sender=Publication)
def create_publication_slug(sender, instance, created, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()