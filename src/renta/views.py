from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.db.models import Count,Sum,Avg
from .models import Factura,Alquiler,Detalle_Alquiler
from django.urls import reverse, reverse_lazy

# Create your views here.

class FacturaListView(generic.ListView):
    model = Factura
    template_name = "index.html"


class FacturaCreateView(generic.CreateView):
    model = Factura
    fields=['numero_factura','cliente','orden','pago']
    template_name = "factura.html"
    success_url = reverse_lazy('renta:index')


class AlquilerCreateView(generic.CreateView):
    model = Alquiler
    fields=['estado','total']
    template_name = "alquiler.html"
    success_url = reverse_lazy('renta:index')


class AlquilerListView(generic.ListView):
    model = Alquiler
    template_name = "list_alquiler.html"


class AlquilerDetailView(generic.DetailView):
    model = Alquiler
    template_name = "info_alquiler.html"


class Detalle_AlquilerCreateView(generic.CreateView):
    model = Detalle_Alquiler
    fields=['orden','maquinaria','cantidad_maquinas','cantidad_horas','subtotal']
    template_name = "detalle_alquiler.html"
    success_url = reverse_lazy('renta:index')


class Detalle_AlquilerListView(generic.ListView):
    model = Detalle_Alquiler
    template_name = "list_detalle_alquiler.html"


class Detalle_AlquilerDeleteView(generic.DeleteView):
    model = Detalle_Alquiler
    template_name = "detalle_delete.html"
    success_url = reverse_lazy('renta:l_detalle')


class Detalle_AlquilerDetailView(generic.DetailView):
    model = Detalle_Alquiler
    template_name = "info_detalle.html"



class FacturaDeleteView(generic.DeleteView):
    model = Factura
    template_name = "f_delete.html"
    success_url = reverse_lazy('renta:index')

def total(request):
    totales=Detalle_Alquiler.objects.all().aggregate(Sum('subtotal'))
    return render(request,'reporte2.html',{'totales':totales})

def promedio(request):
    promedios= Detalle_Alquiler.objects.all().aggregate(Avg('subtotal'))
    return render(request,'reporte3.html',{'promedios':promedios})








