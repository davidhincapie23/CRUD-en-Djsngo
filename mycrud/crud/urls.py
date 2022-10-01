from django.urls import path
from . import views

urlpatterns = [

    # Urls Developers
    path('', views.listDev),
    path('register/', views.createDev),
    path('edit/<slug:slug>', views.editDev, name='editUrl'),
    path('delete/<slug:slug>', views.deleteDev, name='deleteUrl'),


]
