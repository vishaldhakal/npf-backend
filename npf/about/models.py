from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    review = models.TextField()
    avatar = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    rating_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class OurTeam(models.Model):
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.FileField()
    facebook = models.URLField()
    instagram = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()

    def __str__(self):
        return self.name


# our client model
class OurClient(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField()

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    src = models.FileField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    video = models.FileField(
        upload_to="videos/", help_text="Upload your video here", blank=True
    )
    video_url = models.URLField(blank=True)
    poster = models.FileField(upload_to="videos/posters/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if not self.video and not self.video_url:
            raise ValidationError("Either video or video_url must be provided.")
        if self.video and self.video_url:
            raise ValidationError("Only one of video or video_url should be provided.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


# model called donation that has the following fields:
# name: CharField
# email: EmailField
# image = models.FileField() which can be null
# amount: DecimalField
# created_at: DateTimeField


class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.FileField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
