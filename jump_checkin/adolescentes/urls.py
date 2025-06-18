from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_adolescentes, name='listar_adolescentes'),
    path('novo/', views.cadastrar_adolescente, name='cadastrar_adolescente'),
    path('criar/', views.cadastrar_adolescente, name='criar_adolescente'),
    path('editar/<int:id>/', views.editar_adolescente, name='editar_adolescente'),
    path('excluir/<int:id>/', views.excluir_adolescente, name='excluir_adolescente'),
    path('lista/', views.listar_adolescentes, name='lista'),
    path('checkin/', views.checkin_dia, name='checkin_dia'),
]
