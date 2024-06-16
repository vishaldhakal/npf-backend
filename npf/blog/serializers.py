from .models import Author, Category, Tag, Blog, Publication, Event

from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField()

    class Meta:
        model = Author

        fields = [
            "id",
            "name",
            "avatar",
            "quotes",
            "social_links",
            "total_reviews",
            "role",
            "about",
            "verified",
            "phone_number",
            "rating_number",
        ]

    def get_social_links(self, obj):
        return {
            "facebook": obj.facebook,
            "instagram": obj.instagram,
            "linkedin": obj.linkedin,
            "twitter": obj.twitter,
            "whatsapp": obj.whatsapp,
        }


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]  # Only include the name field

    def to_representation(self, instance):
        # Return the name directly
        return instance.name


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]  # Add other fields as necessary

    def to_representation(self, instance):
        # Return the name directly
        return instance.name


# Blog and Publication serializers list without content and hero


class BlogListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Blog
        fields = [
            "id",
            "slug",
            "title",
            "created_at",
            "updated_at",
            "cover",
            "duration",
            "description",
            "category",
            "author",
            "tags",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)


class PublicationListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Publication
        fields = [
            "id",
            "slug",
            "title",
            "created_at",
            "updated_at",
            "cover",
            "duration",
            "description",
            "category",
            "author",
            "tags",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)


class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Blog
        fields = [
            "id",
            "slug",
            "title",
            "hero",
            "created_at",
            "updated_at",
            "cover",
            "duration",
            "description",
            "content",
            "category",
            "author",
            "tags",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)


class PublicationSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Publication
        fields = [
            "id",
            "slug",
            "title",
            "hero",
            "created_at",
            "updated_at",
            "cover",
            "duration",
            "description",
            "content",
            "category",
            "author",
            "tags",
            "pdf",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)


# get publication name and slug only
# create a new field which will be called as path and will be used to create the url
# it should be like /publication/{slug}
# i just want 8 latest publications like this
class PublicationNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = [
            "title",
            "path",
        ]

    def get_path(self, obj):
        return f"/publications/{obj.slug}"


class BlogNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = [
            "title",
            "path",
        ]

    def get_path(self, obj):
        return f"/posts/{obj.slug}"


class EventNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "title",
            "path",
        ]

    def get_path(self, obj):
        return f"/events/{obj.slug}"


class NavigationSerializer(serializers.Serializer):
    blog = serializers.SerializerMethodField()
    publication = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()

    def get_blog(self, obj):
        return {
            "latest_blogs": self.get_latest_blogs(),
            "featured_blogs": self.get_featured_blogs(),
        }

    def get_publication(self, obj):
        return {
            "latest_publications": self.get_latest_publications(),
            "featured_publications": self.get_featured_publications(),
        }

    def get_event(self, obj):
        return {
            "latest_events": self.get_latest_events(),
        }

    def get_latest_blogs(self):
        blogs = Blog.objects.all().order_by("-created_at")[:8]
        return BlogNameSerializer(blogs, many=True).data

    def get_featured_blogs(self):
        blogs = Blog.objects.filter(is_featured=True)
        return BlogNameSerializer(blogs, many=True).data

    def get_latest_publications(self):
        publications = Publication.objects.all().order_by("-created_at")[:8]
        return PublicationNameSerializer(publications, many=True).data

    def get_featured_publications(self):
        publications = Publication.objects.filter(is_featured=True)
        return PublicationNameSerializer(publications, many=True).data

    def get_latest_events(self):
        events = Event.objects.all().order_by("-created_at")[:8]
        return EventNameSerializer(events, many=True).data


class EventListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Event
        fields = [
            "id",
            "slug",
            "title",
            "created_at",
            "updated_at",
            "cover",
            "duration",
            "description",
            "category",
            "author",
            "tags",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)


class EventSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Event
        fields = [
            "id",
            "slug",
            "title",
            "hero",
            "created_at",
            "updated_at",
            "cover",
            "duration",
            "description",
            "content",
            "category",
            "author",
            "tags",
            "pdf",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)
