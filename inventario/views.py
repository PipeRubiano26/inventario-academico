from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Producto


class ProductoListView(ListView):
    model = Producto
    template_name = 'inventario/lista_productos.html'
    context_object_name = 'productos'


class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'categoria', 'cantidad', 'minimo']
    template_name = 'inventario/formulario_producto.html'
    success_url = reverse_lazy('lista_productos')


class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'categoria', 'cantidad', 'minimo']
    template_name = 'inventario/formulario_producto.html'
    success_url = reverse_lazy('lista_productos')


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'inventario/eliminar_producto.html'
    success_url = reverse_lazy('lista_productos')