from .models import DonationContent
from .serializers import DonationContentSerializer
from rest_framework import generics

# Create your views here.


class DonationContentListCreate(generics.ListCreateAPIView):
    queryset = DonationContent.objects.all()
    serializer_class = DonationContentSerializer


class DonationContentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonationContent.objects.all()
    serializer_class = DonationContentSerializer
