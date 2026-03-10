from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='Team DC', description='DC superheroes')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        # Create Activities
        today = timezone.now().date()
        Activity.objects.create(user=users[0], type='Running', duration=30, date=today)
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date=today - timedelta(days=1))
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date=today - timedelta(days=2))
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date=today - timedelta(days=3))

        # Create Workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Strength and flexibility')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
