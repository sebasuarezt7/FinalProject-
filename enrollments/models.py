from django.db import models
from students.models import Student
from courses.models import Course

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    section = models.CharField(max_length=20, default="A")

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} → {self.course}"