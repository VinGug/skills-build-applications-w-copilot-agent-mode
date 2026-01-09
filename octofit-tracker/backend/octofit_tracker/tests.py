from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class BasicModelTests(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='TestActivity', user_email='test@example.com', team='TestTeam')
        self.assertEqual(activity.name, 'TestActivity')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=10)
        self.assertEqual(leaderboard.points, 10)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', description='desc', user_email='test@example.com')
        self.assertEqual(workout.name, 'TestWorkout')
