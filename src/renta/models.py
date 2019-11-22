from django.db import models
from maquinaria.models import Maquinaria
from cliente.models import Cliente
from django.db.models.signals import pre_save, post_save, post_delete

# Create your models here.

class Factura(models.Model):
    """Model definition for Factura."""

    # TODO: Define fields here
    METODO_PAGO=[
        ("ef", "efectivo"),
        ("cd", "tarjeta"),
        ("cq", "cheque"),
    ]
    numero_factura=models.CharField(max_length=12)
    fecha=models.DateField(auto_now_add=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.PROTECT)
    orden=models.OneToOneField("Alquiler",on_delete=models.CASCADE)
    pago=models.CharField(max_length=3,choices=METODO_PAGO)

    class Meta:
        """Meta definition for Factura."""

        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
    
    def __str__(self):
       return str(self.cliente) + " " + str(self.orden.id)

    def total(self):
        return self.orden.total

def factura_post_save_receiver(sender, instance, *args, **kwargs):
    """Calls update_status def from Order Model"""
    instance.orden.actualizar_estado("pa")

post_save.connect(factura_post_save_receiver, sender=Factura)

class Alquiler(models.Model):
    """Model definition for Alquiler."""

    # TODO: Define fields here
    ESTADO_ALQUILER=[
        ("re", "recivida"),
        ("pa", "pagada"),
        ("pr","proceso"),
    ]
    fecha_alquiler=models.DateField(auto_now_add=True)
    maquinaria=models.ManyToManyField(Maquinaria,through="Detalle_Alquiler")
    estado=models.CharField(max_length=3,choices=ESTADO_ALQUILER,default="re")
    total=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)

    class Meta:
        """Meta definition for Alquiler."""

        verbose_name = 'Alquiler'
        verbose_name_plural = 'Alquilers'
    
    def actualizar_total(self):
        total=0
        maquinas = self.detalle_alquiler_set.all()
        for maquinaria in maquinas:
            total += maquinaria.subtotal
        self.total = total
        self.save()

    def actualizar_estado(self,choice):
        self.estado=choice
        self.save()

    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return u'/renta/%d' % self.id

class Detalle_Alquiler(models.Model):
    """Model definition for Detalle_Alquiler."""

    # TODO: Define fields here
    orden=models.ForeignKey(Alquiler,on_delete=models.PROTECT)
    maquinaria=models.ForeignKey(Maquinaria,on_delete=models.CASCADE)
    cantidad_maquinas=models.PositiveIntegerField(default=1)
    cantidad_horas=models.IntegerField(blank=True,null=True)
    subtotal=models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)

    class Meta:
        """Meta definition for Detalle_Alquiler."""

        verbose_name = 'Detalle_Alquiler'
        verbose_name_plural = 'Detalle_Alquilers'
    
    def remover(self):
        return self.maquinaria.remover_from_alquiler()

    def __str__(self):
        return self.maquinaria.nombre_maquinaria

def orden_maquinaria_pre_save_receiver(sender,instance,*args,**kwargs):
    qty=instance.cantidad_horas
    qty1=instance.cantidad_maquinas
    if qty>=1:
        cantidad_horas=instance.maquinaria.fraccion_tiempo
        subtotal=qty*cantidad_horas*qty1
        instance.cantidad_horas=cantidad_horas
        instance.subtotal=subtotal

pre_save.connect(orden_maquinaria_pre_save_receiver, sender=Detalle_Alquiler)

def order_maquinaria_post(sender, instance, *args, **kwargs):
    instance.orden.actualizar_total()

post_save.connect(orden_maquinaria_pre_save_receiver, sender=Detalle_Alquiler)

post_delete.connect(order_maquinaria_post, sender=Detalle_Alquiler)




