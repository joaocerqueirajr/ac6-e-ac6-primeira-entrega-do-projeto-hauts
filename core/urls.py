from django.urls import path
from core import views

app_name='core'
urlpatterns = [

    path('', views.home, name="home"),
    path('contato/', views.contato, name='contato'),
    path('entrar/', views.entrar, name='entrar'),
    path('impacta/', views.impacta, name='impacta'),
    


]