from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Command to load/update the data from the API to the app"

    def handle(self, *args, **options):
