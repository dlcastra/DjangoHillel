# Generated by Django 4.2.5 on 2023-09-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CreateStudent",
            fields=[
                ("student_id", models.IntegerField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("birth_date", models.DateField()),
            ],
        ),
    ]
