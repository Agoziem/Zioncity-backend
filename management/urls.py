from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("studentsapi/", include("Students.urls")),
    path("teachersapi/", include("Teachers.urls")),
    path("adminsapi/", include("Admins.urls")),
    path("resultapi/", include("Results.urls")),
    path("chatroomapi/", include("ChatSystem.urls")),
    path("attendanceapi/", include("Attendance.urls")),
    path("admissionsapi/", include("Admissions.urls")),
    path("Authentication/", include("Authentication.urls")),
    path("cbtapi/", include("CBT.urls")),
    path("paymentsapi/", include("Payments.urls")),
    path("schedulesapi/", include("Schedules.urls")),
    path("analyticsapi/", include("Analytics.urls")),
    path("elibraryapi/", include("Elibrary.urls")),
    path("edugptapi/", include("EduGPT.urls")),
]


if settings.DEBUG_ENV:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header='COG Backend'
admin.site.index_title='Site Administration'
