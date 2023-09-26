from django.urls import path

from . import views

urlpatterns = [
    path("generate-student/", views.create_one_student, name="create_one_student"),
    path(
        "generate-students/",
        views.create_multiply_students,
        name="create_multiply_students",
    ),
]
