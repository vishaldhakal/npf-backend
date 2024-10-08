from rest_framework import serializers
from .models import (
    FAQ,
    Testimonial,
    OurTeam,
    OurClient,
    Video,
    Image,
    Donation,
    Role,
)


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


class OurTeamListSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="role.name")

    class Meta:
        model = OurTeam
        fields = [
            "id",
            "role",
            "name",
            "photo",
            "facebook",
            "instagram",
            "linkedin",
            "twitter",
        ]


class OurTeamSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="role.name")

    class Meta:
        model = OurTeam
        fields = "__all__"


class RoleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class OurClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurClient
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):
    src = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ("src", "title", "description", "created_at")

    def get_src(self, obj):
        return "https://admin.nationalpolicyforum.com" + obj.src.url


class VideoSourceSerializer(serializers.Serializer):
    src = serializers.URLField()
    type = serializers.CharField()


class VideoSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    width = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    sources = serializers.SerializerMethodField()
    poster = serializers.SerializerMethodField()

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

    def get_poster(self, obj):
        return "https://admin.nationalpolicyforum.com" + obj.poster.url

    def get_type(self, obj):
        return "video"

    def get_width(self, obj):
        return 1280

    def get_height(self, obj):
        return 720

    def get_sources(self, obj):
        if obj.video_url:
            return [
                {
                    "src": obj.video_url,
                    "type": "video/mp4",
                }
            ]
        elif obj.video:
            return [
                {
                    "src": "https://admin.nationalpolicyforum.com" + obj.video.url,
                    "type": "video/mp4",
                }
            ]
        return []


# donation serializer
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ["id", "name", "email", "image", "amount", "message"]
