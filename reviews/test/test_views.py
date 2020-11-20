import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from reviews.models import Review, Company
from django.contrib.auth.models import User
from reviews.serializers import ReviewSerializer

from rest_framework.authtoken.models import Token

# initialize the APIClient app
client = Client()


class GetAllReviewsTest(TestCase):
    """ Test module for GET all Reviews API """

    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@consumeraffairs.com", "password_123")
        self.company = Company.objects.create(name="ConsumerAffairs")
        self.review = Review.objects.create(
            rating=1,
            title="Great Company",
            summary="Awesome Company to work",
            ip_address="192.168.1.1",
            company=self.company,
            reviewer=self.user
        )
        self.review = Review.objects.create(
            rating=1,
            title="OK Company",
            summary="I like it",
            ip_address="192.168.1.1",
            company=self.company,
            reviewer=self.user
        )
        self.token = Token.objects.create(user=self.user)
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token.key)}


    def test_get_all_reviews(self):
        # get API response
        response = client.get(reverse('review-list'), **self.header)
        # get data from db
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_all_reviews_without_token(self):
        # get API response
        response = client.get(reverse('review-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GetSingleReviewTest(TestCase):
    """ Test module for GET single Review API """

    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@consumeraffairs.com", "password_123")
        self.company = Company.objects.create(name="ConsumerAffairs")
        self.review = Review.objects.create(
            rating=1,
            title="Great Company",
            summary="Awesome Company to work",
            ip_address="192.168.1.1",
            company=self.company,
            reviewer=self.user
        )
        self.token = Token.objects.create(user=self.user)
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token.key)}

    def test_get_valid_single_review(self):
        response = client.get(
            reverse('review-detail', kwargs={'pk': self.review.pk}), **self.header)
        review = Review.objects.get(pk=self.review.pk)
        serializer = ReviewSerializer(review)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_review(self):
        response = client.get(
            reverse('review-detail', kwargs={'pk': 30}), **self.header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_valid_single_review_without_token(self):
        response = client.get(
            reverse('review-detail', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class CreateNewReviewTest(TestCase):
    """ Test module for inserting a new Review """

    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@consumeraffairs.com", "password_123")
        self.company = Company.objects.create(name="ConsumerAffairs")
        self.valid_payload = {
            'rating': 1,
            'title': "Great Company",
            'summary': "Awesome Company to work",
            'ip_address': "192.168.1.1",
            'company': self.company.id,
            'reviewer': self.user.id
        }
        self.invalid_payload = {
            'rating': 1,
            'title': "",
            'summary': "",
            'ip_address': "192.168.1.1",
            'company': self.company.id,
            'reviewer': self.user.id
        }
        self.token = Token.objects.create(user=self.user)
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token.key)}

    def test_create_valid_review(self):
        response = client.post(
            reverse('review-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            **self.header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_review(self):
        response = client.post(
            reverse('review-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            **self.header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_valid_review_without_token(self):
        response = client.post(
            reverse('review-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class UpdateSingleReviewTest(TestCase):
    """ Test module for updating an existing Review record """

    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@consumeraffairs.com", "password_123")
        self.company = Company.objects.create(name="ConsumerAffairs")
        self.review = Review.objects.create(
            rating=1,
            title="Great Company",
            summary="Awesome Company to work",
            ip_address="192.168.1.1",
            company=self.company,
            reviewer=self.user
        )
        self.valid_payload = {
            'rating': 2,
            'title': "Great Company",
            'summary': "Awesome Company to work",
            'ip_address': "192.168.1.1",
            'company': self.company.id,
            'reviewer': self.user.id
        }
        self.invalid_payload = {
            'rating': 1,
            'title': "",
            'summary': "",
            'ip_address': "192.168.1.1",
            'company': self.company.id,
            'reviewer': self.user.id
        }
        self.token = Token.objects.create(user=self.user)
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token.key)}

    def test_valid_update_review(self):
        response = client.put(
            reverse('review-detail', kwargs={'pk': self.review.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
            **self.header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_review(self):
        response = client.put(
            reverse('review-detail', kwargs={'pk': self.review.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
            **self.header
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_review_without_token(self):
        response = client.put(
            reverse('review-detail', kwargs={'pk': self.review.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeleteSingleReviewTest(TestCase):
    """ Test module for deleting an existing Review record """

    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@consumeraffairs.com", "password_123")
        self.company = Company.objects.create(name="ConsumerAffairs")
        self.review = Review.objects.create(
            rating=1,
            title="Great Company",
            summary="Awesome Company to work",
            ip_address="192.168.1.1",
            company=self.company,
            reviewer=self.user
        )
        self.token = Token.objects.create(user=self.user)
        self.header = {'HTTP_AUTHORIZATION': 'Token {}'.format(self.token.key)}

    def test_valid_delete_review(self):
        response = client.delete(
            reverse('review-detail', kwargs={'pk': self.review.pk}), **self.header)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_review(self):
        response = client.delete(
            reverse('review-detail', kwargs={'pk': 30}), **self.header)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_valid_delete_review_without_token(self):
        response = client.delete(
            reverse('review-detail', kwargs={'pk': self.review.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)