from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import Author, SocialLinks, Category, Tag, Blog, Publication
from .serializers import (
    AuthorSerializer,
    SocialLinksSerializer,
    CategorySerializer,
    TagSerializer,
    BlogSerializer,
    CategoryNameSerializer,
    PublicationSerializer,
    BlogListSerializer,
    PublicationListSerializer,
    PublicationNameSerializer,
    NavigationSerializer,
)


class BlogListCreate(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer

    def get(self, request, *args, **kwargs):
        is_featured = request.GET.get("is_featured")
        is_latest = request.GET.get("is_latest")
        per_page = request.GET.get("per_page")
        category = request.GET.get("category")
        tag = request.GET.get("tag")

        queryset = self.get_queryset()

        if is_featured:
            queryset = queryset.filter(is_featured=True)
        elif is_latest:
            queryset = queryset.order_by("-created_at")[:3]
        elif category:
            queryset = queryset.filter(category__name=category)
            if per_page:
                try:
                    per_page = int(per_page)
                    queryset = queryset[:per_page]
                except ValueError:
                    pass
        elif tag:
            queryset = queryset.filter(tags__name=tag)
            if per_page:
                try:
                    per_page = int(per_page)
                    queryset = queryset[:per_page]
                except ValueError:
                    pass

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BlogRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "slug"


class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class SocialLinksListCreate(generics.ListCreateAPIView):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer


class SocialLinksRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer


class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryNameSerializer(categories, many=True)
        return Response(serializer.data)


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PublicationListCreate(generics.ListCreateAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationListSerializer

    def get(self, request, *args, **kwargs):
        is_featured = request.GET.get("is_featured")
        is_latest = request.GET.get("is_latest")
        per_page = request.GET.get("per_page")
        category = request.GET.get("category")
        tag = request.GET.get("tag")

        queryset = self.get_queryset()

        if is_featured:
            queryset = queryset.filter(is_featured=True)
        elif is_latest:
            queryset = queryset.order_by("-created_at")[:3]
        elif category:
            queryset = queryset.filter(category__name=category)
            if per_page:
                try:
                    per_page = int(per_page)
                    queryset = queryset[:per_page]
                except ValueError:
                    pass
        elif tag:
            queryset = queryset.filter(tags__name=tag)
            if per_page:
                try:
                    per_page = int(per_page)
                    queryset = queryset[:per_page]
                except ValueError:
                    pass

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PublicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    lookup_field = "slug"


class PublicationNameListView(APIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationNameSerializer

    # get only name
    def get(self, request):
        # get latest 8 publications
        publications = Publication.objects.all().order_by("-created_at")[:8]
        serializer = PublicationNameSerializer(publications, many=True)
        return Response(serializer.data)


class NavigationView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = NavigationSerializer(data={})
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
