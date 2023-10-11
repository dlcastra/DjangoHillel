# Generated by Django 4.2.5 on 2023-10-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school", "0001_initial"),
        ("student_generation", "0003_createstudent_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="createstudent",
            name="group",
            field=models.ManyToManyField(related_name="group", to="school.groups"),
        ),
    ]