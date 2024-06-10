from rest_framework import generics
from .models import FAQ, Testimonial, OurTeam, OurClient, Image, Video, Donation
from .serializers import (
    FAQSerializer,
    TestimonialSerializer,
    OurTeamSerializer,
    OurClientSerializer,
    ImageSerializer,
    DonationSerializer,
    VideoSerializer,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from itertools import chain

# Create your views here.


class FAQListCreate(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class TestimonialListCreate(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class TestimonialRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


class OurTeamListCreate(generics.ListCreateAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class OurTeamRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurTeam.objects.all()
    serializer_class = OurTeamSerializer


class OutClientListCreate(generics.ListCreateAPIView):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer


class OutClientRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = OurClient.objects.all()
    serializer_class = OurClientSerializer


class ImageListView(generics.ListAPIView):
    queryset = Image.objects.all().order_by("-created_at")
    serializer_class = ImageSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all().order_by("-created_at")
    serializer_class = VideoSerializer


class ImageVideoListView(APIView):
    def get(self, request, *args, **kwargs):
        images = Image.objects.all()
        videos = Video.objects.all()

        # Serialize the data
        image_serializer = ImageSerializer(images, many=True)
        video_serializer = VideoSerializer(videos, many=True)

        # Combine and sort by created_at
        combined = list(chain(image_serializer.data, video_serializer.data))
        combined.sort(key=lambda x: x["created_at"], reverse=True)

        return Response({"media": combined})


# donation view


class DonationListCreate(generics.ListCreateAPIView):
    queryset = Donation.objects.all().order_by("-created_at")
    serializer_class = DonationSerializer


class DonationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Donation.objects.all().order_by("-created_at")
    serializer_class = DonationSerializer


# get top donors by adding amount of same email and sorting by amount
# should also return the email and amount , latest image uploaded and latest donation message of the same email
class TopDonors(APIView):
    def get(self, request, *args, **kwargs):
        donations = Donation.objects.all()
        # get top donors
        top_donors = {}
        for donation in donations:
            if donation.email in top_donors:
                top_donors[donation.email] += donation.amount
            else:
                top_donors[donation.email] = donation.amount

        # sort top donors by amount
        top_donors = dict(sorted(top_donors.items(), key=lambda x: x[1], reverse=True))

        # get latest donation details for each top donor
        top_donors_info = []
        for email in top_donors:
            latest_donation = (
                Donation.objects.filter(email=email).order_by("-created_at").first()
            )
            if latest_donation:
                donor_info = {
                    "id": latest_donation.id,
                    "name": latest_donation.name,
                    "email": email,
                    "amount": top_donors[email],
                    "message": latest_donation.message,
                    "image": (
                        latest_donation.image.url if latest_donation.image else None
                    ),
                }
                top_donors_info.append(donor_info)

        return Response(top_donors_info[:5])
