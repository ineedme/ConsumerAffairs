from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', "rating", "title", "summary", "ip_address", "submitted_at", "company", "reviewer")
        read_only_fields = ('id',)


