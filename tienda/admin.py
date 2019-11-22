from django.contrib import admin

from .models import  Maquinaria, Cliente, Alquiler

#admin.site.register(Tipo_maquinaria)
admin.site.register(Maquinaria)
admin.site.register(Cliente)
admin.site.register(Alquiler)
