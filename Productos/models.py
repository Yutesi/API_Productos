from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)  # ← campo booleano

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='productos'
    )

    def __str__(self):
        return self.nombre
