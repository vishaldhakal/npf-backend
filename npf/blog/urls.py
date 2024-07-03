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
    path(
        "events/",
        views.EventListCreate.as_view(),
        name="event_list_create",
    ),
    path(
        "events/<str:slug>/",
        views.EventRetrieveUpdateDestroy.as_view(),
        name="event_retrieve_update_destroy",
    ),
    path(
        "opportunity/",
        views.OpportunityListCreate.as_view(),
        name="opportunity_list_create",
    ),
    path(
        "opportunity/<str:slug>/",
        views.OpportunityRetrieveUpdateDestroy.as_view(),
        name="opportunity_retrieve_update_destroy",
    ),
    path(
        "opportunity-type-name/",
        views.OpportunityTypeNameListCreate.as_view(),
        name="opportunity_type_list_create",
    ),
    path(
        "opportunity-type-name/<int:pk>/",
        views.OpportunityTypeNameRetrieveUpdateDestroy.as_view(),
        name="opportunity_type_retrieve_update_destroy",
    ),
    path(
        "opportunity-type/",
        views.OpportunityTypeListCreate.as_view(),
        name="opportunity_type_list_create",
    ),
    path(
        "opportunity-type/<int:pk>/",
        views.OpportunityTypeRetrieveUpdateDestroy.as_view(),
        name="opportunity_type_retrieve_update_destroy",
    ),
    path(
        "jobs/",
        views.JobsListCreate.as_view(),
        name="jobs_list_create",
    ),
    path(
        "jobs/<str:slug>/",
        views.JobsRetrieveUpdateDestroy.as_view(),
        name="jobs_retrieve_update_destroy",
    ),
]
