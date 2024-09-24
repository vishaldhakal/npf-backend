from django.urls import path
from . import views


urlpatterns = [
    path(
        "donation-content/",
        views.DonationContentListCreate.as_view(),
        name="donation-list-create",
    ),
    path('newsletter-members/', views.NewsletterMemberListCreateView.as_view(), name='newsletter-member-list-create'),
    path('newsletter-members/<int:pk>/', views.NewsletterMemberRetrieveUpdateDestroyView.as_view(), name='newsletter-member-detail'),
]
