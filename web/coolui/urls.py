from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.projectView, name='project'),
    path('contact/', views.contactView, name='contact'),
    path('', views.indexView, name='index'),
]