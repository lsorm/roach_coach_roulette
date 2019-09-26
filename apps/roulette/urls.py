from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index), # to homepage
    url(r'^optionsDisplay$', views.optionsDisplay), # to page where they will choose distance
    url(r'^roulett$', views.roulett), # will process their request and redirect to resultsDisplay
    url(r'^resultsDisplay$', views.resultsDisplay), # to page that will display results
    url(r'^viewInfo/(?P<result_id>\d+)$', views.viewInfo), #to page that will display details about specific restaurant
    url(r'^GoBack$', views.goBack),# to go back to homepage and start over "delete session"
    url(r'^loginReg$',views.loginReg),# to login and registration page
    url(r'^newUser$', views.newUser),# to create the new user
    url(r'^dashboard$', views.dashboard), # to display their personal dashboard
    url(r'^edit$', views.editFaves), # to edit the user's favorites to add notes.
    url(r'^options_submit$', views.optionsSubmit)
]
