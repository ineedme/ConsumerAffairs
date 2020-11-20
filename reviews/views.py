# from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Revivews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
