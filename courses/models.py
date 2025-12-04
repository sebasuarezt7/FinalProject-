from django.db import models

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    schedule = models.CharField(max_length=50)  # e.g. "Mon 2–4 PM"
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.title}"