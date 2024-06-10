from django.urls import path
from . import views


urlpatterns = [
    path(
        "donation-content/",
        views.DonationContentListCreate.as_view(),
        name="donation-list-create",
    ),
]
