from django.urls import path

from . import views

app_name="renta"
urlpatterns = [
    path("renta/",views.FacturaListView.as_view(),name="index"),
    path("listalquiler/",views.AlquilerListView.as_view(),name="list_alquiler"),
    path("alquilerinfo/<int:pk>", views.AlquilerDetailView.as_view(), name="info_alquiler"),
    path("factura/", views.FacturaCreateView.as_view(), name="create_f"),
    path("alquiler/", views.AlquilerCreateView.as_view(), name="create_a"),
    path("detalle/", views.Detalle_AlquilerCreateView.as_view(), name="create_da"),
    path('fdelete/<int:pk>', views.FacturaDeleteView.as_view(), name='invoice_delete'),
    path('ddelete/<int:pk>', views.Detalle_AlquilerDeleteView.as_view(), name='d_delete'),
     path("detalleinfo/<int:pk>", views.Detalle_AlquilerDetailView.as_view(), name="detalle_detalle"),
    path("l_detalle/",views.Detalle_AlquilerListView.as_view(),name="l_detalle"),
    path('reporte2/',views.total,name="suma_total"),
    path('reporte3/',views.promedio,name="promedio"),
]