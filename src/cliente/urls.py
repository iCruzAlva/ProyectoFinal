from django.urls import path

from . import views

app_name="cliente"
urlpatterns = [
    path("list/",views.ClienteListView.as_view(),name="list_costumer"),
    path("<int:pk>/info", views.ClienteDetailView.as_view(), name="info_costumer"),
    path("create/", views.ClienteCreateView.as_view(), name="create"),
    path("<int:pk>/", views.ClienteUpdateView.as_view(), name='f_update'),
     path('delete/<int:pk>', views.ClienteDeleteView.as_view(), name='costumer_delete'),
    path('menu/',views.dashboard,name="dashboard"),
]