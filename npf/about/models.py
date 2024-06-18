from django.db import models
from django.core.exceptions import ValidationError


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    review = models.TextField()
    avatar = models.ImageField(upload_to="testimonials/avatars/")
    created_at = models.DateTimeField(auto_now_add=True)
    rating_number = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    hierarchy_level = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["hierarchy_level"]


class OurTeam(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="team/photos/")
    bio = models.TextField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    hierarchy_level = models.IntegerField(default=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["hierarchy_level"]


class OurClient(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="clients/images/")

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    src = models.ImageField(upload_to="images/")
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
    poster = models.ImageField(upload_to="videos/posters/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        if not self.video and not self.video_url:
            raise ValidationError("Either video or video_url must be provided.")
        if self.video and self.video_url:
            raise ValidationError("Only one of video or video_url should be provided.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Donation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to="donations/images/", null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
