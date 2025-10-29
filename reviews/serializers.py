from rest_framework import serializers
from reviews.models import Review, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name',)


class ReviewSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source='company', write_only=True
    )

    class Meta:
        model = Review
        fields = ('id', "rating", "title", "summary", "ip_address", "submitted_at", "company", "company_id", "reviewer")
        read_only_fields = ('id', 'reviewer', 'ip_address')
