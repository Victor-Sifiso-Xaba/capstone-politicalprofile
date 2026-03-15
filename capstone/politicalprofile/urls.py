from django.urls import path, include
from . import views

app_name = 'politicalprofile'

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('values/', views.values_view, name='values'),
]