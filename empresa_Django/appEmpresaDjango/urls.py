from django.urls import path
from . import views

urlpatterns = [
    path('', views.DepartamentoListView.as_view(), name='index'),
    path('departamentos/<int:pk>/', views.DepartamentoDetailView.as_view(), name='detail'),
    path('departamentos/create', views.DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/<int:departamento_id>/empleados', views.EmpleadoListView.as_view(), name='empleados'),
    path('empleados/create', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='detail_empleado'),

]
