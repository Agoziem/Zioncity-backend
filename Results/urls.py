from django.urls import path
from .gettingresultviews import *
from .creatingresultviews import *

urlpatterns = [
    path('',getRoutes, name='getRoutes'),

    # for getting results
    path('getresultsummary/', get_result_summary, name='getresultsummary'),
    path('getsubjectresult/', get_subject_result, name='getsubjectresult'),
    path('getsubjectresults/', get_subject_results, name='getsubjectresults'),
    path('getannualresultsummary/', get_annual_result_summary, name='getannualresultsummary'),
    path('getannualsubjectresult/', get_annual_subject_result, name='getannualsubjectresult'),
    path('getannualsubjectresults/', get_annual_subject_results, name='getannualsubjectresults'),
    path('getresultsummary/', get_result_summary, name='getresultsummary'),
    
    # for creating results
    path('getcreatingResultRoutes/', getcreatingResultRoutes, name='getcreatingResultRoutes'),
    path('getResults/', getResults, name='getResults'),
    path('updateResult/<int:result_id>', updateResult, name='updateResult'),
    path('deleteResult/<int:result_id>', deleteResult, name='deleteResult'),
    path('postResults/', postResults, name='postResults'),

    path('getResultSummaries/', getResultSummaries, name='getResultSummaries'),
    path('postResultSummaries/', postResultSummaries, name='postResultSummaries'),

    path('getAnnualResults/', getAnnualResults, name='getAnnualResults'),
    path('updateAnnualResult/<int:result_id>', updateAnnualResult, name='updateAnnualResult'),
    path('postAnnualResults/', postAnnualResults, name='postAnnualResults'),

    path('getAnnualResultSummaries/', getAnnualResultSummaries, name='getAnnualResultSummaries'),
    path('postAnnualResultSummaries/', postAnnualResultSummaries, name='postAnnualResultSummaries'),
    
]

