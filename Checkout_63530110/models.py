from django.db import models
from Productos.models import Producto

# Create your models here.
"""
#CLASES PARA LOS PRODUCTOS

#Clase para el tipo de electrodomestico
class TipoElectrodomestico(models.Model):
    nombre = models.CharField(max_length=200)
    foto = models.ImageField(blank=True, null=True)


#Clase para el producto
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoElectrodomestico, on_delete=models.CASCADE)
    precio = models.IntegerField()
    #el atributo tipo TextField es más grande que el CharField y puede llevar o no max_length
    descripcion = models.TextField()
    foto = models.ImageField(blank=True, null=True)
    calificacion = models.FloatField()


#Clase para los comentarios de usuarios
class Comentario(models.Model):
    usuario = models.CharField(max_length=100)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    calificacion = models.FloatField()
    fecha = models.DateField()
    contenido = models.CharField(max_length=500)
"""
#CLASES PARA EL CHECKOUT

#Clase para el Carrito de compras
class CarritoCompras(models.Model):
    usuario = models.CharField(max_length=100)
    #el atributo auto_now_add es para que agregue automáticamente la fecha actual
    fecha = models.DateField(auto_now_add=True)
    dcto = models.FloatField()
    cantMinima = models.IntegerField(default=0)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario + " - " + str(self.fecha)
    
    def total(self):
        pass

    def numArt(self):
        pass

#Clase para el articulo en el carrito de compras
class Articulo(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    #producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.carrito.__str__() + " / " + self.producto.__str___()
    
    def subtotal(self):
        #subtotal = Precio Unitario * cantidad
        return self.cantidad*self.producto.precio


#Clase para la informacion de envío de la compra
class InfoEnvio(models.Model):
    carrito = models.ForeignKey(CarritoCompras, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    departamento = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)

    def __str__(self):
        return self.carrito.__str__()
    


