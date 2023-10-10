from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import TeachersForm, GroupsForm
from .models import Teachers, Groups


def main_page(request):
    return render(request, "main_page.html")


""" -- Part of a view for teacher model -- """


def create_teacher(request):
    if request.method == "GET":
        form = TeachersForm()
        return render(request, "teachers_form.html", {"form": form})

    form = TeachersForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("get_teachers_list")

    return render(request, "teachers_form.html", {"form": form})


def get_teachers_list(request):
    teachers = Teachers.objects.all()
    return render(request, "get_teachers_list.html", {"teachers": teachers})


def edit_teacher(request, pk):
    teacher = Teachers.objects.get(pk=pk)
    if request.method == "GET":
        form = TeachersForm(instance=teacher)
        return render(request, "edit_teacher.html", {"teacher": form})

    form = TeachersForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect(reverse("get_teachers_list"))

    return render(request, "edit_teacher.html", {"teacher": form})


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teachers, pk=pk)
    if request.method == "GET":
        form = TeachersForm(instance=teacher)
        return render(request, "edit_teacher.html", {"teacher": form})

    form = TeachersForm(request.POST, instance=teacher)
    if form.is_valid():
        teacher.delete()
        return redirect(reverse("get_teachers_list"))


""" -- Part of a view for group model -- """


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


def edit_group(request, pk):
    group = Groups.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupsForm(instance=group)
        return render(request, "edit_group.html", {"group": form})

    form = GroupsForm(request.POST, instance=group)
    if form.is_valid():
        form.save()
        return redirect(reverse("get_group_list"))

    return render(request, "edit_group.html", {"group": form})


def delete_group(request, pk):
    group = get_object_or_404(Groups, pk=pk)
    if request.method == "GET":
        form = GroupsForm(instance=group)
        return render(request, "edit_group.html", {"group": form})

    form = GroupsForm(request.POST, instance=group)
    if form.is_valid():
        group.delete()
        return redirect(reverse("get_group_list"))
