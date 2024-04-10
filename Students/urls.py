from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('<int:school_id>/', views.getallStudents),
    path('<int:school_id>/<int:class_id>/', views.getStudents),
    path('create/<int:school_id>/<int:class_id>/', views.createStudent),
    path('student/<int:student_id>/', views.getStudent),
    path('update/<int:student_id>/', views.updateStudent),
    path('delete/<int:student_id>/', views.deleteStudent),
]