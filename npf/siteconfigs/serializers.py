from .models import DonationContent,NewsletterMember
from rest_framework import serializers


class DonationContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationContent
        fields = "__all__"

class NewsletterMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterMember
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, data):
        if data.get('member_type') == 'contributing':
            required_fields = ['name', 'education', 'phone_number', 'contribution_area', 'contribution_type']
            for field in required_fields:
                if not data.get(field):
                    raise serializers.ValidationError(f"{field} is required for contributing members.")
        return data