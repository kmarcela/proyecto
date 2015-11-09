from django.db import models

class venta(models.Model):
    producto = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)

    def ingresar(self):
        self.save()

    def __str__(self):
        return self.producto
