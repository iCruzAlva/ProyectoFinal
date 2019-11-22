from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
from django.views import generic
from .models import Cliente
from django.urls import reverse, reverse_lazy
# Create your views here.


class ClienteListView(generic.ListView):
    model = Cliente
    template_name = "list.html"


class ClienteDetailView(generic.DetailView):
    model = Cliente
    template_name = "detail.html"

class ClienteCreateView(generic.CreateView):
    model = Cliente
    fields=['nombre','apellido','nit','direccion','telefono','correo']
    template_name = "f_create.html"

class ClienteUpdateView(generic.UpdateView):
    model = Cliente
    fields=['nombre','apellido','nit','direccion','telefono','correo']
    template_name = "f_update.html"

class ClienteDeleteView(generic.DeleteView):
    model = Cliente
    template_name="delete.html"
    success_url = reverse_lazy('cliente:list_costumer')
    


def dashboard(request):
    return render(request,'dashboard.html')