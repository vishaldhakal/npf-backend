from .models import DonationContent
from rest_framework import serializers


class DonationContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationContent
        fields = "__all__"
