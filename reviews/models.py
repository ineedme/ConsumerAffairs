from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Company(models.Model):
    """
    Company Model
    Defines the attributes of a Company
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Reviews Model
    Defines the attributes of a Review
    """
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    title = models.CharField(max_length=64)
    summary = models.TextField(max_length=10000)
    ip_address = models.GenericIPAddressField(unpack_ipv4=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['submitted_at']
