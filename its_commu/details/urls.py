from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('info/', TemplateView.as_view(template_name='info.html'), name='info'),
    path('info_its/', views.info_its, name='info_its'),
    path('info_year/', views.info_year, name='info_year'),
]
