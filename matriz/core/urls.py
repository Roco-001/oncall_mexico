from django.urls import path
from . import views
from .views import HomePageView,CategoriaListView,CategoriaDetail, TablaDetail, GuardiasEspecialistasListView,GuardiasEspecialistasUpdateView, GuardiasEspecialistasDeleteView,GuardiaSemanalCreate, GuardiaListView, GuardiaDetail



app_name= 'core'
urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('categorias/', CategoriaListView.as_view(), name="categoria_list"),
	path('<int:pk>/', CategoriaDetail.as_view(), name="categoria_detail"),
	path('tabla/<int:pk>/', TablaDetail.as_view(), name="tabla_detail"),

	path('create_guardia_semanal/', GuardiaSemanalCreate.as_view(), name='guardiaSemanal_create'),

	path('guardias/especialistas/', GuardiasEspecialistasListView.as_view(), name="guardias_especialistas_list"),
	path('guardias/especialistas/update/<int:pk>/', GuardiasEspecialistasUpdateView.as_view(), name="guardias_especialistas_update"),
	path('guardias/especialistas/delete/<int:pk>/', GuardiasEspecialistasDeleteView.as_view(), name="guardias_especialistas_delete"),

	path('guardias/soportes/', GuardiaListView.as_view(), name="guardias_soportes_list"),

	path('guardia/<int:pk>/', GuardiaDetail.as_view(), name="guardia_detail"),



]