from django.db import models


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    subject = models.CharField(max_length=50)
