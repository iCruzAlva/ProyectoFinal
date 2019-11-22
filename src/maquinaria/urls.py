from django.urls import path

from . import views

app_name="maquinaria"
urlpatterns = [
    path("listadom/",views.MaquinariaListView.as_view(),name="list_machina"),
    path("info/<int:pk>", views.MaquinariaDetailView.as_view(), name="info_machina"),
    path("mcreate/", views.MaquinariaCreateView.as_view(), name="create_m"),
    path("<int:pk>/", views.MaquinariaUpdateView.as_view(), name='m_update'),
    path('mdelete/<int:pk>', views.MaquinariaDeleteView.as_view(), name='machina_delete'),
    path('reporte/',views.conteo,name="rep"),
]