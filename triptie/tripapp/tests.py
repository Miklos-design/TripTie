from django.core.exceptions import ValidationError
from django.urls import reverse
from django_registration.forms import User
from django.test import TestCase, RequestFactory
from tripapp.models import TripPlan
from tripapp.views import ProfileView, EditProfileView, MyTripPlansView, MyLikesView


class TripPlanMethodTests(TestCase):
    def test_end_date_after_start_date(self):
        """
        Ensures that the end date is after or equal to the start date for a TripPlan.
        """
        user = User.objects.create_user(username='testuser', password='password')

        # Test case where end date is after start date
        trip_plan_valid = TripPlan(
            user=user,
            title='Test Trip',
            description='This is a test trip.',
            destination_city='Test City',
            start_date='2024-03-01',
            end_date='2024-03-10',
            is_private=False,
        )
        trip_plan_valid.clean()  # Should not raise any validation error

        # Test case where end date is before start date
        trip_plan_invalid = TripPlan(
            user=user,
            title='Test Trip',
            description='This is a test trip.',
            destination_city='Test City',
            start_date='2024-03-10',
            end_date='2024-03-01',
            is_private=False,
        )
        with self.assertRaises(ValidationError):
            trip_plan_invalid.clean()  # Should raise a validation error


class ProfileViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tripapp:profile', kwargs={'username': self.user.username})

    def test_profile_view(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = ProfileView.as_view()(request, username=self.user.username)
        self.assertEqual(response.status_code, 200)


class EditProfileViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tripapp:edit_profile', kwargs={'username': self.user.username})

    def test_edit_profile_view(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = EditProfileView.as_view()(request, username=self.user.username)
        self.assertEqual(response.status_code, 200)


class MyTripPlansViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tripapp:my_trip_plans', kwargs={'username': self.user.username})

    def test_my_trip_plans_view(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = MyTripPlansView.as_view()(request, username=self.user.username)
        self.assertEqual(response.status_code, 200)


class MyLikesViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.url = reverse('tripapp:my_likes', kwargs={'username': self.user.username})

    def test_my_likes_view(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = MyLikesView.as_view()(request, username=self.user.username)
        self.assertEqual(response.status_code, 200)
