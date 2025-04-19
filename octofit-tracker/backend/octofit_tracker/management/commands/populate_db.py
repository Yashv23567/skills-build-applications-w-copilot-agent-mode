from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Users
        user1 = User.objects.create(id=ObjectId(), email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(id=ObjectId(), email="jane.smith@example.com", name="Jane Smith", password="password123")
        user3 = User.objects.create(id=ObjectId(), email="alice.wonder@example.com", name="Alice Wonder", password="password123")
        user4 = User.objects.create(id=ObjectId(), email="bob.builder@example.com", name="Bob Builder", password="password123")

        # Create Teams
        team1 = Team.objects.create(name="Team Alpha", members=[{"id": str(ObjectId()), "member_id": str(user1.id)}])
        team2 = Team.objects.create(name="Team Beta", members=[{"id": str(ObjectId()), "member_id": str(user2.id)}])
        team3 = Team.objects.create(name="Team Gamma", members=[{"id": str(ObjectId()), "member_id": str(user3.id)}])
        team4 = Team.objects.create(name="Team Delta", members=[{"id": str(ObjectId()), "member_id": str(user4.id)}])

        # Create Activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-18")
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45, date="2025-04-18")
        Activity.objects.create(user=user3, activity_type="Swimming", duration=60, date="2025-04-18")
        Activity.objects.create(user=user4, activity_type="Hiking", duration=120, date="2025-04-18")

        # Create Leaderboard entries
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)
        Leaderboard.objects.create(team=team3, points=90)
        Leaderboard.objects.create(team=team4, points=70)

        # Create Workouts
        Workout.objects.create(name="Morning Run", description="A quick morning run", duration=30)
        Workout.objects.create(name="Evening Yoga", description="Relaxing yoga session", duration=60)
        Workout.objects.create(name="Afternoon Swim", description="A refreshing swim session", duration=60)
        Workout.objects.create(name="Mountain Hike", description="A challenging hike", duration=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
