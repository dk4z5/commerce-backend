from django.urls import path

from . import views

urlpatterns = [
    path('vendas/', views.VendasView.as_view(), name='vendas-view'),
    path('retirada-produtos/', views.RetiradaProdutoView.as_view(), name='retiradas-view'),
    path('precos/', views.PrecosView.as_view(), name='retiradas-view'),
]

