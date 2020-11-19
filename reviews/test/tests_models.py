from django.contrib.auth.models import User
from django.test import TestCase
from reviews.models import Company, Review

class CompanyTest(TestCase):
    """ Test Module for Company Model """

    def setUp(self):
        self.company = Company.objects.create(name="ConsumerAffairs")

    def test_company_creation(self):
        consumer_affairs = Company.objects.get(name='ConsumerAffairs')

        self.assertEqual(str(consumer_affairs), 'ConsumerAffairs')


class ReviewTest(TestCase):
    """ Test Module for Company Model """

    def setUp(self):
        self.user = User.objects.create_user("admin", "admin@consumeraffairs.com", "password_123")
        self.company = Company.objects.create(name="ConsumerAffairs")
        self.review= Review.objects.create(
            rating=1,
            title="Great Company",
            summary="As good as it can be",
            ip_address="192.168.1.1",
            company=self.company,
            reviewer=self.user
        )

    def test_company_creation(self):
        consumer_affairs_review = Review.objects.get(title="Great Company")
        self.assertEqual(str(consumer_affairs_review), "Great Company")
