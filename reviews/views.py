from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication,
                              TokenAuthentication,
                              ]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the reviews
        for the currently authenticated user.
        """
        return Review.objects.filter(reviewer=self.request.user)

    def perform_create(self, serializer):
        ip = self.request.META.get('REMOTE_ADDR')
        serializer.save(reviewer=self.request.user, ip_address=ip)
