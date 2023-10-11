from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    birth_date = models.DateField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}, {self.surname}, {self.patronymic}, {self.birth_date}, {self.subject}"


class Groups(models.Model):
    group_name = models.CharField(max_length=100)
    curator = models.ForeignKey(Teachers, on_delete=models.PROTECT)

    def __str__(self):
        return self.group_name
