from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.views import generic
from .models import Maquinaria
from django.db.models import Count
from django.urls import reverse, reverse_lazy
# Create your views here.


class MaquinariaListView(generic.ListView):
    model = Maquinaria
    template_name = "list_m.html"


class MaquinariaDetailView(generic.DetailView):
    model = Maquinaria
    template_name = "detail_m.html"


class MaquinariaCreateView(generic.CreateView):
    model = Maquinaria
    fields=['nombre_maquinaria','imagen','tipo_maquinaria','fraccion_tiempo','marca','estado']
    template_name = "m_create.html"


class MaquinariaUpdateView(generic.UpdateView):
    model = Maquinaria
    fields=['nombre_maquinaria','imagen','tipo_maquinaria','fraccion_tiempo','marca','estado']
    template_name = "m_update.html"


class MaquinariaDeleteView(generic.DeleteView):
    model = Maquinaria
    template_name="delete_m.html"
    success_url = reverse_lazy('maquinaria:list_machina')

def conteo(request):
    estados=Maquinaria.objects.values('estado').order_by('estado').annotate(count=Count('estado'))
    return render(request,'reporte1.html',{'estados':estados})


    