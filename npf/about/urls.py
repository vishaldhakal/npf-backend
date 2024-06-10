from django.urls import path
from . import views

urlpatterns = [
    path("faq/", views.FAQListCreate.as_view(), name="faq_list_create"),
    path(
        "faq/<int:pk>/",
        views.FAQRetrieveUpdateDestroy.as_view(),
        name="faq_retrieve_update_destroy",
    ),
    path(
        "testimonial/",
        views.TestimonialListCreate.as_view(),
        name="testimonial_list_create",
    ),
    path(
        "testimonial/<int:pk>/",
        views.TestimonialRetrieveUpdateDestroy.as_view(),
        name="testimonial_retrieve_update_destroy",
    ),
    path("our-team/", views.OurTeamListCreate.as_view(), name="our_team_list_create"),
    path(
        "our-team/<int:pk>/",
        views.OurTeamRetrieveUpdateDestroy.as_view(),
        name="our_team_retrieve_update_destroy",
    ),
    path(
        "our-client/",
        views.OutClientListCreate.as_view(),
        name="our_client_list_create",
    ),
    path(
        "our-client/<int:pk>/",
        views.OutClientRetrieveUpdateDestroy.as_view(),
        name="our_client_retrieve_update_destroy",
    ),
    path("images/", views.ImageListView.as_view(), name="image-list"),
    path("videos/", views.VideoListView.as_view(), name="video-list"),
    path("media/", views.ImageVideoListView.as_view(), name="image-video-list"),
    path("donations/", views.DonationListCreate.as_view(), name="donation-list-create"),
    path(
        "donations/<int:pk>/",
        views.DonationRetrieveUpdateDestroy.as_view(),
        name="donation-retrieve-update-destroy",
    ),
    # top donors
    path("top-donations/", views.TopDonors.as_view(), name="top-donors"),
]
