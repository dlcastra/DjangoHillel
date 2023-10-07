from django.shortcuts import render, redirect

from .forms import TeachersForm, GroupsForm
from .models import Teachers, Groups


def main_page(request):
    return render(request, "main_page.html")


def teacher_form(request):
    if request.method == "GET":
        form = TeachersForm()
        return render(request, "teachers_form.html", {"form": form})

    form = TeachersForm(request.POST)
    if form.is_valid():
        teacher = Teachers.objects.create(
            first_name=request.POST["first_name"],
            surname=request.POST["surname"],
            patronymic=request.POST["patronymic"],
            birth_date=request.POST["birth_date"],
            subject=request.POST["subject"],
        )
        return redirect("get_teachers_list")

    return render(request, "teachers_form.html", {"form": form})


def get_teachers_list(request):
    teachers = Teachers.objects.all()
    return render(request, "get_teachers_list.html", {"teachers": teachers})


def group_form(request):
    if request.method == "GET":
        form = GroupsForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupsForm(request.POST)
    if form.is_valid():
        form.save()

        return redirect("get_group_list")


def get_group_list(request):
    groups = Groups.objects.all()
    return render(request, "get_group_list.html", {"groups": groups})
