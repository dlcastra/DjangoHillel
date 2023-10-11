from django.db import models

from school.models import Groups


class CreateStudent(models.Model):
    student_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    group = models.ManyToManyField(Groups, related_name="group")

    def __str__(self):
        return f"{self.first_name, self.first_name}"
