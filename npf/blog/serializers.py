from .models import (
    Author,
    Category,
    Tag,
    Blog,
    Publication,
    Event,
    Opportunity,
    OpportunityType,
    Jobs,
)
from rest_framework import serializers

# serializers from about app
from about.models import Role


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
        fields = ["name"]

    def to_representation(self, instance):
        return instance.name


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["name"]

    def to_representation(self, instance):
        return instance.name


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


class RolePath(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Role
        fields = ["name", "path"]

    def get_path(self, obj):
        return f"/teams-type/{obj.slug}"


class PublicationNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ["title", "path"]

    def get_path(self, obj):
        return f"/publications/{obj.slug}"


class BlogNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ["title", "path"]

    def get_path(self, obj):
        return f"/posts/{obj.slug}"


class EventNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ["title", "path"]

    def get_path(self, obj):
        return f"/events/{obj.slug}"


class OpportunityNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()

    class Meta:
        model = Opportunity
        fields = ["title", "path"]

    def get_path(self, obj):
        return f"/opportunities/{obj.slug}"


class OpportunityTypeNameOnlySerializer(serializers.ModelSerializer):
    # serialize such that i get array of strings
    class Meta:
        model = OpportunityType
        fields = ["title"]

    def to_representation(self, instance):
        return instance.title


class OpportunityTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpportunityType
        fields = "__all__"


class OpportunityTypeNameSerializer(serializers.ModelSerializer):
    path = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    class Meta:
        model = OpportunityType
        fields = ["title", "path", "children"]

    def get_path(self, obj):
        return f"/opportunities-type/{obj.slug}"

    def get_children(self, obj):
        if obj.has_subcategories():
            return [
                {
                    "subheader": obj.title,
                    "items": [
                        {
                            "title": subcategory.title,
                            "path": f"/opportunities-type/{subcategory.slug}",
                        }
                        for subcategory in obj.get_subcategories()
                    ],
                }
            ]
        else:
            return []


class NavigationSerializer(serializers.Serializer):
    blog = serializers.SerializerMethodField()
    publication = serializers.SerializerMethodField()
    event = serializers.SerializerMethodField()
    our_team = serializers.SerializerMethodField()
    opportunity = serializers.SerializerMethodField()

    def get_our_team(self, obj):
        return {
            "roles": self.get_roles(),
        }

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

    def get_opportunity(self, obj):
        return {
            "latest_opportunities": self.get_latest_opportunities(),
            "opportunity_types": self.get_opportunity_types(),
        }

    def get_latest_blogs(self):
        blogs = Blog.objects.all().order_by("-created_at")[:6]
        return BlogNameSerializer(blogs, many=True).data

    def get_featured_blogs(self):
        latest_blogs = Blog.objects.all().order_by("-created_at")[:6]
        blogs = (
            Blog.objects.filter(is_featured=True)
            .order_by("-created_at")
            .exclude(id__in=latest_blogs.values_list("id", flat=True))[:6]
        )
        return BlogNameSerializer(blogs, many=True).data

    def get_latest_publications(self):
        publications = Publication.objects.all().order_by("-created_at")[:6]
        return PublicationNameSerializer(publications, many=True).data

    def get_featured_publications(self):
        latest_publications = Publication.objects.all().order_by("-created_at")[:6]
        publications = (
            Publication.objects.filter(is_featured=True)
            .order_by("-created_at")
            .exclude(id__in=latest_publications.values_list("id", flat=True))[:6]
        )
        return PublicationNameSerializer(publications, many=True).data

    def get_latest_events(self):
        events = Event.objects.all().order_by("-created_at")[:8]
        return EventNameSerializer(events, many=True).data

    def get_roles(self):
        roles = Role.objects.all().order_by("hierarchy_level")
        return RolePath(roles, many=True).data

    def get_latest_opportunities(self):
        opportunities = Opportunity.objects.all().order_by("-created_at")[:8]
        return OpportunityNameSerializer(opportunities, many=True).data

    def get_opportunity_types(self):
        types = OpportunityType.objects.filter(parent__isnull=True)
        data = OpportunityTypeNameSerializer(types, many=True).data

        opportunity_types = {
            "title": "Opportunities",
            "path": "#",
            "children": [
                {
                    "subheader": "Opportunities",
                    "items": [
                        {"title": item["title"], "path": item["path"]}
                        for item in data
                        if not item["children"]
                    ],
                }
            ],
        }

        for item in data:
            children = item.get("children")
            if children:
                opportunity_types["children"].append(children[0])

        return opportunity_types


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


class OpportunityListSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = OpportunityTypeNameOnlySerializer()
    author = AuthorSerializer()

    class Meta:
        model = Opportunity
        fields = [
            "id",
            "slug",
            "title",
            "created_at",
            "updated_at",
            "cover",
            "category",
            "duration",
            "description",
            "category",
            "author",
            "tags",
        ]

    def get_tags(self, obj):
        return obj.tags.values_list("name", flat=True)


class OpportunitySerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    category = serializers.CharField(source="category.name", read_only=True)
    author = AuthorSerializer()

    class Meta:
        model = Opportunity
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


# class Jobs(models.Model):
#     title = models.CharField(max_length=2000)
#     slug = models.SlugField(unique=True, null=True, blank=True, max_length=1000)
#     description = models.TextField(max_length=2000, null=True, blank=True)
#     location = models.CharField(max_length=2000)
#     salary = models.CharField(max_length=2000)
#     type = models.CharField(max_length=2000)
#     experience = models.CharField(max_length=2000)
#     level = models.CharField(max_length=2000)
#     skills = models.ManyToManyField(Skills)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     cover = models.ImageField(upload_to="covers/")
#     deadline = models.DateField()
#     description = models.TextField(max_length=2000)
#     content = models.TextField()
#     urgent = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title


class JobsListSerializers(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Jobs
        fields = [
            "id",
            "slug",
            "title",
            "created_at",
            "updated_at",
            "cover",
            "location",
            "salary",
            "type",
            "experience",
            "level",
            "skills",
            "deadline",
            "description",
            "urgent",
        ]

    def get_skills(self, obj):
        return obj.skills.values_list("name", flat=True)


class JobsSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Jobs
        fields = [
            "id",
            "slug",
            "title",
            "created_at",
            "updated_at",
            "cover",
            "location",
            "salary",
            "type",
            "experience",
            "level",
            "skills",
            "deadline",
            "description",
            "content",
            "urgent",
        ]

    def get_skills(self, obj):
        return obj.skills.values_list("name", flat=True)
