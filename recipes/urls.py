from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    # <int:id> usamos para notificar qual receita queremos impimir
    # o int serve para permitir apenas numeros no link
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
