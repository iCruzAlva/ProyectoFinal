from django.db import models



class Maquinaria(models.Model):
    nombre= models.CharField(max_length=40)
    #estado= models.BooleanField(null=True)
    alquilado = 'alq'
    disponible = 'dis'
    opciones = [
        (alquilado, 'alquilado'),
        (disponible, 'disponible'),
    ]
    estado = models.CharField(
        max_length=3,
        choices=opciones,
        default=disponible,
    )
    #tipo = models.ForeignKey(Tipo_maquinaria,on_delete= models.PROTECT)
   


    class Meta:
        """Meta definition for Maquinaria."""

        verbose_name = 'Maquinaria'
        verbose_name_plural = 'Maquinarias'

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre= models.CharField(max_length=40)
    telefono= models.CharField(max_length=40)
    nit= models.CharField(default='C/F',max_length=13)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre

class Alquiler(models.Model):
    nombre= models.CharField(max_length=40)
    cliente = models.ForeignKey(Cliente,on_delete= models.PROTECT)
    #maquinaria = models.ForeignKey(Maquinaria,on_delete= models.PROTECT)
    

    class Meta:
        """Meta definition for Alquiler."""

        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquilers'

    def __str__(self):
       return self.nombre

        



