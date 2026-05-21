from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    minimo = models.IntegerField(default=5)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def stock_bajo(self):
        return self.cantidad <= self.minimo

    def __str__(self):
        return self.nombre