from django.urls import path

from . import views
app_name = 'myfirstsite'
urlpatterns = [
    path('', views.index, name='index'),
]