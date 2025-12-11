import csv
from django.core.management.base import BaseCommand
from courses.models import Course


class Command(BaseCommand):
    help = "Import courses from courses_data.csv into the database"

    def handle(self, *args, **options):
        file_path = "courses_data.csv"  

        try:
            with open(file_path, newline="", encoding="utf-8") as csvfile:
                reader = csv.DictReader(csvfile)

                count = 0
                for row in reader:
                    code = row.get("code")
                    title = row.get("title")
                    capacity = row.get("capacity") or 30  

                    Course.objects.get_or_create(
                        code=code,
                        defaults={
                            "title": title,
                            "capacity": capacity,
                        },
                    )
                    count += 1

            self.stdout.write(self.style.SUCCESS(
                f"Imported {count} courses from {file_path}"
            ))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(
                f"File {file_path} not found. Put it next to manage.py"
            ))