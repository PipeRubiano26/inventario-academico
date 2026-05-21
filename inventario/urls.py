from django.urls import path
from .views import (
    ProductoListView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView
)

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='lista_productos'),

    path('productos/nuevo/', ProductoCreateView.as_view(), name='crear_producto'),

    path('productos/editar/<int:pk>/',
         ProductoUpdateView.as_view(),
         name='editar_producto'),

    path('productos/eliminar/<int:pk>/',
         ProductoDeleteView.as_view(),
         name='eliminar_producto'),
]