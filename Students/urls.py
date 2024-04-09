from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('<int:school_id>/<int:class_id>/', views.getStudents),
    path('create/<int:school_id>/<int:class_id>/', views.createStudent),
    path('<int:student_id>/', views.getStudent),
    path('<int:student_id>/update/', views.updateStudent),
    path('<int:student_id>/delete/', views.deleteStudent),
]