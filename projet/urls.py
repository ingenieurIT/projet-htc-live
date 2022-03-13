from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('login-admin/', AdminLogin.as_view(), name="loginadmin"),
    path('logout/', views.logout_page, name='logout'),
    path('enregistrer/', views.enregistrer, name='enregistrer'),
    path('', views.accueil, name='accueil'),
    path('ajouter_art/', views.ajouter_art, name='ajouter_art'),
    path('ordi/<str:pk>/', views.detail_pc, name='ordi'),
    path('like/', views.like, name='like'),
]
