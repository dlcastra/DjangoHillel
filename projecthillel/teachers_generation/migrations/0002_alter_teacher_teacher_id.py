# Generated by Django 4.2.5 on 2023-09-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teachers_generation", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="teacher_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
