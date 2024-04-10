from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes),
    path('<int:school_id>/', getTeachers),
    path('create/<int:school_id>/', createTeacher),
    path('teacher/<int:teacher_id>/', getTeacher),
    path('update/<int:teacher_id>/', updateTeacher),
    path('delete/<int:teacher_id>/', deleteTeacher),
]

