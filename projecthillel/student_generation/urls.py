from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.create_one_student, name="create_one_student"),
    path(
        "generate-students/",
        views.create_multiply_students,
        name="create_multiply_students",
    ),
    path("create-student/", views.create_student, name="create_student"),
    path("list-students/", views.get_student_list, name="get_student_list"),
    path("edit-student/<int:pk>", views.edit_student, name="edit_student"),
    path("to-group/<int:pk>", views.add_student_to_group, name="add_student_to_group"),
]
