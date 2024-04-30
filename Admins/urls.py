from django.urls import path
from .views.views import *
from .views.academicsessionviews import *
from .views.classesviews import *
from .views.schoolviews import *
from .views.subjectallocationviews import *
from .views.subjectsviews import *
from .views.termviews import *
from .views.newsletterviews import *


urlpatterns = [
    path('',getRoutes, name='routes'),
    path('terms/',getTerms, name='terms'),
    path('terms/create/',createTerm, name='create_term'),
    path('terms/<int:term_id>/',getTerm, name='term'),
    path('terms/<int:term_id>/update/',updateTerm, name='update_term'),
    path('terms/<int:term_id>/delete/',deleteTerm, name='delete_term'),

    path('academicsessions/', getAcademicSessions, name='academic_sessions'),
    path('academicsessions/create/', createAcademicSession, name='create_academic_session'),
    path('academicsessions/<int:session_id>/',getAcademicSession, name='academic_session'),
    path('academicsessions/<int:session_id>/update/',updateAcademicSession, name='update_academic_session'),
    path('academicsessions/<int:session_id>/delete/',deleteAcademicSession, name='delete_academic_session'),

    path('classes/', getClasses, name='classes'),
    path('classes/create/', createClass, name='create_class'),
    path('classes/<int:class_id>/', getClass, name='class'),
    path('classes/<int:class_id>/update/', updateClass, name='update_class'),
    path('classes/<int:class_id>/delete/', deleteClass, name='delete_class'),

    path('subjects/', getSubjects, name='subjects'),
    path('subjects/create/', createSubject, name='create_subject'),
    path('subjects/<int:subject_id>/', getSubject, name='subject'),
    path('subjects/<int:subject_id>/update/', updateSubject, name='update_subject'),
    path('subjects/<int:subject_id>/delete/', deleteSubject, name='delete_subject'),
    
    path('schools/', getSchools, name='schools'),
    path('schools/create/', createSchool, name='create_school'),
    path('schools/<int:school_id>/', getSchool, name='school'),
    path('schools/<int:school_id>/update/', updateSchool, name='update_school'),
    path('schools/<int:school_id>/delete/', deleteSchool, name='delete_school'),

    path('confirmAdmin/', confirmAdmin, name='confirm_admin'),
    path('admins/<int:school_id>/', getAdmins, name='admins'),
    path('admins/<int:school_id>/create/', createAdmin, name='create_admin'),
    path('admins/<int:school_id>/<int:admin_id>/', getAdmin, name='admin'),
    path('admins/<int:admin_id>/update/', updateAdmin, name='update_admin'),
    path('admins/<int:admin_id>/delete/', deleteAdmin, name='delete_admin'),

    path('subjectallocations/<int:school_id>/', getSubjectAllocations, name='subject_allocations'),
    path('subjectallocations/<int:school_id>/create/', createSubjectAllocation, name='create_subject_allocation'),
    path('subjectallocations/<int:school_id>/<int:subjectallocation_id>/', getSubjectAllocation, name='subject_allocation'),
    path('subjectallocations/<int:subjectallocation_id>/update/', updateSubjectAllocation, name='update_subject_allocation'),
    path('subjectallocations/<int:subjectallocation_id>/delete/', deleteSubjectAllocation, name='delete_subject_allocation'),

    path('get_newsletters/<int:school_id>/', get_newsletters, name='get_newsletters'),
    path('get_newsletter/<int:session_id>/<int:term_id>/', get_newsletter, name='get_newsletters'),
    path('add_newsletter/<int:session_id>/<int:term_id>/', add_newsletter, name='add_newsletter'),
    path('update_newsletter/<int:newsletter_id>/', update_newsletter, name='update_newsletter'),
    path('delete_newsletter/<int:newsletter_id>/', delete_newsletter, name='delete_newsletter'),

]
