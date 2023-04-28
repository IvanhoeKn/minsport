from django.urls import path

from . import views

app_name = "fspru"
urlpatterns = [
    path('', views.index, name='index'),
    path('contests', views.contests, name='contests'),
    path('contests/<int:contest_id>', views.contest_description, name='contest_description'),
    path('contests/<int:contest_id>/enter', views.contest_enter, name='contest_enter'),
    path('login', views.login_index, name="login_index"),
    path('logout', views.logout, name="logout"),
    path('my_contests', views.user_contests, name="user_contests"),
    path('registration', views.registration_index, name="registration_index"),
]