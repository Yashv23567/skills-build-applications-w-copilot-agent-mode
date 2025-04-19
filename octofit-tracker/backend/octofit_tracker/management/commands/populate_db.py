from bson import ObjectId
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout, TeamMember

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create Users
        user1 = User.objects.create(id=ObjectId(), email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(id=ObjectId(), email="jane.smith@example.com", name="Jane Smith", password="password123")

        # Create Teams
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")

        # Add members to teams
        team1.members = [{"id": str(ObjectId()), "member_id": str(user1.id)}]
        team2.members = [{"id": str(ObjectId()), "member_id": str(user2.id)}]
        team1.save()
        team2.save()

        # Create Activities
        Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-18")
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45, date="2025-04-18")

        # Create Leaderboard entries
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)

        # Create Workouts
        Workout.objects.create(name="Morning Run", description="A quick morning run", duration=30)
        Workout.objects.create(name="Evening Yoga", description="Relaxing yoga session", duration=60)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
