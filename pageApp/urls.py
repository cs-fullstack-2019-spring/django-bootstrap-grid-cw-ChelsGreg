from django.urls import path
from . import views


# routes to functions
urlpatterns = [
    path('', views.index, name='index'),
    path('pageTwo', views.pageTwo, name='pageTwo'),
    path('pageThree', views.pageThree, name='pageThree'),
]