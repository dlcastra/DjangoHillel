from django.urls import path

from school.views import (
    create_teacher,
    get_teachers_list,
    edit_teacher,
    group_form,
    get_group_list,
    edit_group,
    delete_group,
)

urlpatterns = [
    # Part for teachers
    path("teacher/", create_teacher, name="teacher_form"),
    path("teachers/", get_teachers_list, name="get_teachers_list"),
    path("edit-teacher/<int:pk>", edit_teacher, name="edit_teacher"),
    # Part for groups
    path("group/", group_form, name="group_form"),
    path("groups/", get_group_list, name="get_group_list"),
    path("edit-group/<int:pk>", edit_group, name="edit_group"),
    path("delete-group/<int:pk>", delete_group, name="delete_group"),
]
