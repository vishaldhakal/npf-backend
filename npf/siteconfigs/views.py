from .models import DonationContent, NewsletterMember
from .serializers import DonationContentSerializer, NewsletterMemberSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class DonationContentListCreate(generics.ListCreateAPIView):
    queryset = DonationContent.objects.all()
    serializer_class = DonationContentSerializer


class DonationContentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = DonationContent.objects.all()
    serializer_class = DonationContentSerializer


class NewsletterMemberListCreateView(generics.ListCreateAPIView):
    queryset = NewsletterMember.objects.all()
    serializer_class = NewsletterMemberSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated(), IsAdminUser()]
        return []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class NewsletterMemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsletterMember.objects.all()
    serializer_class = NewsletterMemberSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)