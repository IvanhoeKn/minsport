from django.urls import path

from . import views

app_name = "fspru"
urlpatterns = [
    path('', views.index, name='index'),
    path('contests', views.contests, name='contests'),
    path('contests/<int:contest_id>', views.contest_description, name='contest_description'),
]