from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('section/<str:section_type>/', views.section_detail, name='section_detail'),
]
