from django.urls import path
from . import views

# urls

urlpatterns = [
    path("blog/", views.BlogListCreate.as_view(), name="blog_list_create"),
    path(
        "blog/<str:slug>/",
        views.BlogRetrieveUpdateDestroy.as_view(),
        name="blog_retrieve_update_destroy",
    ),
    path("author/", views.AuthorListCreate.as_view(), name="author_list_create"),
    path(
        "author/<int:pk>/",
        views.AuthorRetrieveUpdateDestroy.as_view(),
        name="author_retrieve_update_destroy",
    ),
    path(
        "social-links/",
        views.SocialLinksListCreate.as_view(),
        name="social_links_list_create",
    ),
    path(
        "social-links/<int:pk>/",
        views.SocialLinksRetrieveUpdateDestroy.as_view(),
        name="social_links_retrieve_update_destroy",
    ),
    path("category/", views.CategoryListCreate.as_view(), name="category_list_create"),
    path(
        "category/<int:pk>/",
        views.CategoryRetrieveUpdateDestroy.as_view(),
        name="category_retrieve_update_destroy",
    ),
    path(
        "category-name/",
        views.CategoryListView.as_view(),
        name="category_name_list_create",
    ),
    path("tag/", views.TagListCreate.as_view(), name="tag_list_create"),
    path(
        "tag/<int:pk>/",
        views.TagRetrieveUpdateDestroy.as_view(),
        name="tag_retrieve_update_destroy",
    ),
    # publication
    path(
        "publication/",
        views.PublicationListCreate.as_view(),
        name="publication_list_create",
    ),
    path(
        "publication/<str:slug>/",
        views.PublicationRetrieveUpdateDestroy.as_view(),
        name="publication_retrieve_update_destroy",
    ),
    # publication name and slug only
    path(
        "publication-name/",
        views.PublicationNameListView.as_view(),
        name="publication_name_list_create",
    ),
    path(
        "nav-links/",
        views.NavigationView.as_view(),
        name="nav_links_list_create",
    ),
]
