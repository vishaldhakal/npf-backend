from django.db import models

# Create your models here.


# a text field for donation page content
class DonationContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
    

class NewsletterMember(models.Model):
    MEMBER_TYPES = [
        ('supporting', 'Supporting Member'),
        ('contributing', 'Contributing Member'),
    ]

    CONTRIBUTION_TYPES = [
        ('intellectual', 'Intellectually'),
        ('volunteer', 'Volunteer'),
        ('financial', 'Financially'),
    ]

    email = models.EmailField()
    member_type = models.CharField(max_length=20, choices=MEMBER_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Fields for contributing members
    name = models.CharField(max_length=255, blank=True, null=True)
    education = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    contribution_area = models.TextField(blank=True, null=True)
    contribution_type = models.CharField(max_length=20, choices=CONTRIBUTION_TYPES, blank=True, null=True)

    def __str__(self):
        return f"{self.email} - {self.get_member_type_display()}"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.member_type == 'contributing':
            if not all([self.name, self.education, self.phone_number, self.contribution_area, self.contribution_type]):
                raise ValidationError("All fields are required for contributing members.")
        else:
            # Clear contributing member fields if the member type is 'supporting'
            self.name = None
            self.education = None
            self.phone_number = None
            self.contribution_area = None
            self.contribution_type = None

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Newsletter Member"
        verbose_name_plural = "Newsletter Members"
