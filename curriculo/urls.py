from django.urls import path, include
from curriculo import views

app_name='curriculo'
urlpatterns = [

    path('', include('core.urls')),
    path('novo/', views.novo_curso, name='novo_curso'),
    path('<str:sigla>/', views.curso, name='curso'),

]