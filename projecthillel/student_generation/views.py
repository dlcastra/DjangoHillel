from django.http import HttpResponse
from faker import Faker

from .models import CreateStudent


fake = Faker()


def create_one_student(request):
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date()

    student = CreateStudent(first_name=first_name, last_name=last_name, birth_date=birth_date)
    student.save()

    return HttpResponse('Ви успішно згенерували випадкові дані студента!')


def create_multiply_students(request):

    try:
        count = int(request.GET.get('count', 0))

        if count <= 100:
            for _ in range(count):
                first_name = fake.first_name()
                last_name = fake.last_name()
                birth_date = fake.date()

                student = CreateStudent(first_name=first_name, last_name=last_name, birth_date=birth_date)
                student.save()

            return HttpResponse(f'Ви успішно знерували дані {count} студентів/та')

        return HttpResponse('Нажаль Ви не можете згенерувати більше 100 студентів')

    except ValueError:
        return HttpResponse('Для генераціі потрібно ввести число')
