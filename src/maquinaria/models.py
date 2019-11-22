from django.db import models
from django.db.models import Count

# Create your models here.
class Tipo_Maquinaria(models.Model):
    """Model definition for Tipo_Maquinaria."""

    # TODO: Define fields here
    nombre_tipo=models.CharField(max_length=30)
    descripcion=models.TextField(null=True)

    class Meta:
        """Meta definition for Tipo_Maquinaria."""

        verbose_name = 'Tipo_Maquinaria'
        verbose_name_plural = 'Tipo_Maquinarias'

    def __str__(self):
        return self.nombre_tipo

class Maquinaria(models.Model):
    """Model definition for Maquinaria."""
#definir unidad de ventas 
    # TODO: Define fields here
    nombre_maquinaria=models.CharField(max_length=60)
    imagen=models.ImageField(upload_to="images")
    tipo_maquinaria=models.ForeignKey(Tipo_Maquinaria,on_delete=models.PROTECT)
    fraccion_tiempo=models.DecimalField(max_digits=6,decimal_places=2,verbose_name="Precio por hora")
    marca=models.CharField(max_length=40)
    ESTADO_OPCION=[
        ("D","Disponible"),
        ("A","Alquilada"),
    ]
    estado=models.CharField(max_length=4,choices=ESTADO_OPCION)

    class Meta:
        """Meta definition for Maquinaria."""

        verbose_name = 'Maquinaria'
        verbose_name_plural = 'Maquinarias'

    def __str__(self):
       return self.nombre_maquinaria
    
    def get_absolute_url(self):
        return u'/maquinaria/%d' % self.id
    


