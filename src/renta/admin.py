from django.contrib import admin
from .models import Detalle_Alquiler,Alquiler,Factura
# Register your models here.
admin.site.register(Detalle_Alquiler)
admin.site.register(Alquiler)
admin.site.register(Factura)