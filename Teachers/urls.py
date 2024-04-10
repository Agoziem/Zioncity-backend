from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes),
    path('<int:school_id>/', getTeachers),
    path('create/<int:school_id>/', createTeacher),
    path('teacher/<int:teacher_id>/', getTeacher),
    path('<int:teacher_id>/update/', updateTeacher),
    path('<int:teacher_id>/delete/', deleteTeacher),
]

