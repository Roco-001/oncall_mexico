from django.contrib import admin
from .models import *



@admin.register(Categoria)
class CategoriaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')




@admin.register(Empresa)
class EmpresaProject(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name','created', 'updated')
    list_filter = ('categoria', )


@admin.register(TablaEscalacion)
class TablaEscalacionProject(admin.ModelAdmin):
    list_display = ('empresa',)





@admin.register(GuardiaEspecialista)
class GuardiaEspecialistaProject(admin.ModelAdmin):

    list_display = ('guardia', 'fecha_inicio', 'fecha_fin')
    readonly_fields = ('created', 'updated')




@admin.register(Guardia)
class GuardiaProject(admin.ModelAdmin):

    list_display = ('name', )
    search_fields = ('name',)





