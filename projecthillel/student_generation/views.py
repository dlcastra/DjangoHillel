from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404

from faker import Faker

from .forms import StudentForm, AddToGroup
from .models import CreateStudent

fake = Faker()

""" --- Generation of one or more random students  --- """


def generation_student():
    first_name = fake.first_name()
    last_name = fake.last_name()
    birth_date = fake.date()

    student = CreateStudent(
        first_name=first_name, last_name=last_name, birth_date=birth_date
    )
    student.save()


def create_one_student(request):
    generation_student()

    return HttpResponse("Ви успішно згенерували випадкові дані студента!")


def create_multiply_students(request):
    try:
        count = int(request.GET.get("count", 0))
    except ValueError:
        return HttpResponse("Для генерації потрібно ввести число")

    if count <= 0 or 0 > 100:
        return HttpResponse(
            "Ви не можете згенерувати меньше одного або більше ніж 100 студентів"
        )

    for _ in range(count):
        generation_student()

    return HttpResponse(f"Ви успішно знерували дані {count} студентів/та")


""" --- CRUD with the CreateStudent model ---"""


def create_student(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "create_student.html", {"student": form})

    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("get_student_list")


def get_student_list(request):
    students = CreateStudent.objects.all()
    return render(request, "get_student_list.html", {"students": students})


def edit_student(request, pk):
    student = get_object_or_404(CreateStudent, pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "edit_student.html", {"student": form})

    form = StudentForm(request.POST, instance=student)
    if "delete" in request.POST:
        student.delete()
        return redirect("get_student_list")

    if form.is_valid():
        form.save()
        return redirect(reverse("get_student_list"))

    return render(request, "edit_student.html", {"student": form})


def add_student_to_group(request, pk):
    student = get_object_or_404(CreateStudent, pk=pk)
    if request.method == "GET":
        form = AddToGroup(instance=student)
        return render(request, "add_to_group.html", {"form": form, "student": student})

    form = AddToGroup(request.POST, instance=student)
    if form.is_valid():
        form.save()
        return redirect("get_student_list")
