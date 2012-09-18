"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from leaderboard import Leaderboard
from django.contrib.auth.models import User

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ViewTest(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.leaderboard_g1 = Leaderboard('game1')
        self.leaderboard_g2 = Leaderboard('game2')

        #get the users
        joan = User.objects.get(username='joan')
        mads = User.objects.get(username='mads')

    def test_listing_high_scores(self):
        # create some records
        self.leaderboard_g1.rank_member(joan.pk, 10)
        self.leaderboard_g1.rank_member(mads.pk, 4)
        self.leaderboard_g1.rank_member(joan.pk, 16)
        self.leaderboard_g1.rank_member(mads.pk, 20)

