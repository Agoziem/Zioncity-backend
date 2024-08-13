from django.urls import path
from .views.Studentsviews import *
from .views.Formteachersviews import *
from .views.Teachersviews import *

urlpatterns = [
    path('',getRoutes, name='getRoutes'),

    # for getting results
    path('getsubjectresult/', get_subject_result, name='getsubjectresult'),
    path('getsubjectresults/', get_subject_results, name='getsubjectresults'),
    path('getannualresultsummary/', get_annual_subject_results, name='getannualresultsummary'),

    path('getsubjectannualresult/', get_annual_subject_result, name='getannualsubjectresult'),
    path('getsubjectannualresults/', get_annual_subject_results, name='getannualsubjectresults'),
    
    # for creating results
    path('getResults/', getResults, name='getResults'),
    path('getResult/<int:result_id>/', getResult, name='getResult'),
    path('updateResult/<int:result_id>/', updateResult, name='updateResult'),
    path('postResults/', postResults, name='postResults'),
    path('unpublishResults/',unpublishResults, name='unpublishResults'),

    path('getResultSummaries/', getResultSummaries, name='getResultSummaries'),
    path('postResultSummaries/', postResultSummaries, name='postResultSummaries'),
    path('unpublishResultSummaries/', unpublishResultSummaries, name='unpublishResultSummaries'),

    path('getAnnualResults/', getAnnualResults, name='getAnnualResults'),
    path('getAnnualResult/<int:result_id>/', getAnnualResult, name='getAnnualResult'),
    path('updateAnnualResult/<int:result_id>/', updateAnnualResult, name='updateAnnualResult'),
    path('postAnnualResults/', postAnnualResults, name='postAnnualResults'),
    path('unpublishAnnualResults/', unpublishAnnualResults, name='unpublishAnnualResults'),

    path('getAnnualResultSummaries/', getAnnualResultSummaries, name='getAnnualResultSummaries'),
    path('postAnnualResultSummaries/', postAnnualResultSummaries, name='postAnnualResultSummaries'),
    path('unpublishAnnualResultSummaries/', unpublishAnnualResultSummaries, name='unpublishAnnualResultSummaries'),
    
]

