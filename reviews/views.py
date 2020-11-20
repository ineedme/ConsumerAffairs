from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication,
                              TokenAuthentication,
                              ]
    permission_classes = [IsAuthenticated]
