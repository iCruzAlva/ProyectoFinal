from django.db import models

# Create your models here.
class Cliente(models.Model):
    """Model definition for Cliente."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    nit = models.CharField(max_length=20,blank=True, default="C/F")
    direccion = models.CharField(max_length=30,blank=True, default="Ciudad")
    telefono = models.CharField(max_length=16)
    correo = models.EmailField(blank=True)

    class Meta:
        """Meta definition for Cliente."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def get_absolute_url(self):
        return u'/cliente/%d' % self.id 


    def __str__(self):
       return self.nombre+" "+self.apellido

