from django.urls import path

from school.views import teacher_form, get_teachers_list, group_form, get_group_list, main_page

urlpatterns = [
    path("teacher/", teacher_form, name="teacher_form"),
    path("teachers/", get_teachers_list, name="get_teachers_list"),
    path("group/", group_form, name="group_form"),
    path("groups/", get_group_list, name="get_group_list"),
]
