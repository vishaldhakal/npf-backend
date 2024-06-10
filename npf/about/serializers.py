from rest_framework import serializers
from .models import FAQ, Testimonial, OurTeam, OurClient, Video, Image, Donation


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

    # sort by created_at
    ordering = ["-created_at"]


class OurTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurTeam
        fields = "__all__"


class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClient
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("src", "title", "description", "created_at")


class VideoSourceSerializer(serializers.Serializer):
    src = serializers.URLField()
    type = serializers.CharField()


class VideoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    sources = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = (
            "type",
            "title",
            "description",
            "poster",
            "width",
            "height",
            "created_at",
            "sources",
        )

    def get_type(self, obj):
        return "video"

    def get_width(self, obj):
        return 1280

    def get_height(self, obj):
        return 720

    def get_sources(self, obj):
        return [{"src": obj.video.url, "type": "video/mp4"}]


# donation serializer
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ["id", "name", "email", "image", "amount", "message"]
