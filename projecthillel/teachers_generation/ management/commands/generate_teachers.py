from django.core.management.base import BaseCommand
from faker import Faker

from projecthillel.teachers_generation.models import Teacher

fake = Faker()


class Command(BaseCommand):
    help = "Add the specified number of teachers to the database"

    def add_arguments(self, parser):
        parser.add_argument("number", type=int)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            teacher = Teacher.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                birth_date=fake.date(),
                subject=fake.job(),
            )

            self.stdout.write(
                self.style.SUCCESS(
                    "The teacher has been successfully added to the database, his id: '%s'" % teacher.id
                )
            )
