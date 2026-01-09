from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.EmailField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user_email = models.EmailField()
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan', 'team': 'Marvel'},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica', 'team': 'Marvel'},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': 'DC'},
            {'email': 'wonderwoman@dc.com', 'username': 'WonderWoman', 'team': 'DC'},
        ]
        for u in users:
            User.objects.create_user(email=u['email'], username=u['username'], password='test1234')

        # Create activities
        Activity.objects.create(name='Running', user_email='ironman@marvel.com', team='Marvel')
        Activity.objects.create(name='Swimming', user_email='captain@marvel.com', team='Marvel')
        Activity.objects.create(name='Flying', user_email='batman@dc.com', team='DC')
        Activity.objects.create(name='Lasso', user_email='wonderwoman@dc.com', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        Workout.objects.create(name='Chest Day', description='Bench press and pushups', user_email='ironman@marvel.com')
        Workout.objects.create(name='Shield Training', description='Shield throws and defense', user_email='captain@marvel.com')
        Workout.objects.create(name='Gadget Training', description='Batmobile and gadgets', user_email='batman@dc.com')
        Workout.objects.create(name='Amazon Training', description='Strength and agility', user_email='wonderwoman@dc.com')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
