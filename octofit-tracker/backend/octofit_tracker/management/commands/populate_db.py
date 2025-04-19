from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Add a confirmation prompt to prevent accidental data deletion
        confirm = input("This will delete all existing data and repopulate the database. Are you sure? (yes/no): ")
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.WARNING('Operation cancelled.'))
            return

        # Add logging for each step
        self.stdout.write(self.style.NOTICE('Clearing existing data...'))
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write(self.style.NOTICE('Creating users...'))
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", password="password123")
        user3 = User.objects.create(email="alice.wonder@example.com", name="Alice Wonder", password="password123")
        user4 = User.objects.create(email="bob.builder@example.com", name="Bob Builder", password="password123")

        self.stdout.write(self.style.NOTICE('Creating teams...'))
        team1 = Team.objects.create(name="Team Alpha")
        team2 = Team.objects.create(name="Team Beta")
        team3 = Team.objects.create(name="Team Gamma")
        team4 = Team.objects.create(name="Team Delta")

        # Update team members population using add()
        team1.members.add(user1)
        team2.members.add(user2)
        team3.members.add(user3)
        team4.members.add(user4)

        self.stdout.write(self.style.NOTICE('Creating activities...'))
        Activity.objects.create(user=user1, activity_type="Running", duration=30, date="2025-04-18")
        Activity.objects.create(user=user2, activity_type="Cycling", duration=45, date="2025-04-18")
        Activity.objects.create(user=user3, activity_type="Swimming", duration=60, date="2025-04-18")
        Activity.objects.create(user=user4, activity_type="Hiking", duration=120, date="2025-04-18")

        self.stdout.write(self.style.NOTICE('Creating leaderboard entries...'))
        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)
        Leaderboard.objects.create(team=team3, points=90)
        Leaderboard.objects.create(team=team4, points=70)

        self.stdout.write(self.style.NOTICE('Creating workouts...'))
        Workout.objects.create(name="Morning Run", description="A quick morning run", duration=30)
        Workout.objects.create(name="Evening Yoga", description="Relaxing yoga session", duration=60)
        Workout.objects.create(name="Afternoon Swim", description="A refreshing swim session", duration=60)
        Workout.objects.create(name="Mountain Hike", description="A challenging hike", duration=120)

        self.stdout.write(self.style.SUCCESS('Database populated with test data'))
