from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thor'),
            User(email='metalgeek@mhigh.edu', name='Tony Stark'),
            User(email='zerocool@mhigh.edu', name='Steve Rogers'),
            User(email='crashoverride@mhigh.edu', name='Natasha Romanoff'),
            User(email='sleeptoken@mhigh.edu', name='Bruce Banner'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        team = Team(name='Avengers')
        team.save()
        team.members.set(User.objects.all())

        # Create activities
        activities = [
            Activity(user=users[0], activity_type='Cycling', duration=60, date=date(2025, 4, 1)),
            Activity(user=users[1], activity_type='Crossfit', duration=120, date=date(2025, 4, 2)),
            Activity(user=users[2], activity_type='Running', duration=90, date=date(2025, 4, 3)),
            Activity(user=users[3], activity_type='Strength Training', duration=30, date=date(2025, 4, 4)),
            Activity(user=users[4], activity_type='Swimming', duration=75, date=date(2025, 4, 5)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0], score=100),
            Leaderboard(user=users[1], score=90),
            Leaderboard(user=users[2], score=95),
            Leaderboard(user=users[3], score=85),
            Leaderboard(user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event', duration=60),
            Workout(name='Crossfit', description='Training for a crossfit competition', duration=120),
            Workout(name='Running Training', description='Training for a marathon', duration=90),
            Workout(name='Strength Training', description='Training for strength', duration=30),
            Workout(name='Swimming Training', description='Training for a swimming competition', duration=75),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
