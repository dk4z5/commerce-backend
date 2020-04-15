from django.urls import path

from . import views

urlpatterns = [
    path('estoques/', views.EstoqueView.as_view(), name='estoque-view'),
    path('estoques/depth/', views.EstoqueDepthView.as_view(), name='estoque-depth-view'),
    path('estoques/vencidos/', views.EstoqueVencidoView.as_view(), name='estoque-vencido-view'),
    path('estoques/<int:pk>/', views.EstoquePartialView.as_view(), name='estoque-partial-view'),
    path('produtos/', views.ProdutoView.as_view(), name='produtos-view'),
    path('produtos/<int:pk>/', views.ProdutoPartialView.as_view(), name='produto-partial-view'),
    path('produtos/faltas/', views.ProdutoFaltaView.as_view(), name='produto-faltas-view'),
]

