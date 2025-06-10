from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_adolescentes, name='listar_adolescentes'),
    path('novo/', views.cadastrar_adolescente, name='cadastrar_adolescente'),
]
