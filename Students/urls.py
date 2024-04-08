from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('studentsapi/<int:school_id>/<int:class_id>/', views.getStudents),
    path('studentsapi/create/<int:school_id>/<int:class_id>/', views.createStudent),
    path('studentsapi/<int:student_id>/', views.getStudent),
    path('studentsapi/<int:student_id>/update/', views.updateStudent),
    path('studentsapi/<int:student_id>/delete/', views.deleteStudent),
]