from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes),
    path('teachersapi/<int:school_id>/', getTeachers),
    path('teachersapi/create/<int:school_id>/', createTeacher),
    path('teachersapi/<int:teacher_id>/', getTeacher),
    path('teachersapi/<int:teacher_id>/update/', updateTeacher),
    path('teachersapi/<int:teacher_id>/delete/', deleteTeacher),
]

