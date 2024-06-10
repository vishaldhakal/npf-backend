from django.db import models

# Create your models here.


# a text field for donation page content
class DonationContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
