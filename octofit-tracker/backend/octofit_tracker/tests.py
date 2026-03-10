from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        self.dc = Team.objects.create(name='Team DC', description='DC superheroes')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.marvel, is_superhero=True)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Spider-Man')

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
