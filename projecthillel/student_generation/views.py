from django.http import HttpResponse

from faker import Faker

from .models import CreateStudent

fake = Faker()


def generation_student():
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date()

    student = CreateStudent(first_name=first_name, last_name=last_name, birth_date=birth_date)
    # student = CreateStudent.objects.create(first_name=first_name, last_name=last_name, birth_date=birth_date)
    student.save()


def create_one_student(request):
    generation_student()

    return HttpResponse('Ви успішно згенерували випадкові дані студента!')


def create_multiply_students(request):
    try:
        count = int(request.GET.get('count', 0))

        if count > 0 <= 100:
            for _ in range(count):
                generation_student()

            return HttpResponse(f'Ви успішно знерували дані {count} студентів/та')

    except ValueError:
        return HttpResponse('Для генераціі потрібно ввести число')

    return HttpResponse('Ви не можете згенерувати меньше одного або більше ніж 100 студентів')
