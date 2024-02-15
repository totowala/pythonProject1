from django.urls import path
from .import views

urlpatterns = [
    path('<int:id>', views.index,name='index'),
    path('', views.home,name='home'),
    path('form/', views.form,name='form'),
    path('Create/', views.Create,name='Create'),
]