# Generated by Django 4.2.5 on 2023-10-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_generation", "0004_alter_createstudent_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="createstudent",
            name="phone",
            field=models.CharField(default=None, max_length=15, null=True),
        ),
    ]
