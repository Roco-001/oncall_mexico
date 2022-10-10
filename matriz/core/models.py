from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# Create your models here.

NIVEL = (
    (1, 'Especialista'),
    (2, 'Supervisor'),
    (3, 'Jefe de área'),
    (4, 'Gerente de área'),
    (5, 'Gerente'),
)

def extensiones_validas(value):
    value = str(value)
    extensiones_validas = ['jpg', 'jpeg', 'png']
    extension = value.split('.')[1].lower()

    if extension not in extensiones_validas:
        raise ValidationError("Archivos permitidos: .jpg, .jpeg, .png")


def extensiones_validas_adjunto(value):
    value = str(value)
    extensiones_validas = ['pdf']
    extension = value.split('.')[1].lower()

    if extension not in extensiones_validas:
        raise ValidationError("Solo permitimos archivos: .pdf")


class Categoria(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre de la Categoria", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name



class Empresa(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="get_categoria",
                                verbose_name="Categoria")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-created"]

    def __str__(self):
        return self.name


class TablaEscalacion(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="get_empresa",
                                verbose_name="Empresa")
    excel = models.FileField(max_length=200, verbose_name="Adjunta El documento", upload_to= 'documents', blank=True, null=True, validators=[extensiones_validas_adjunto])

    imagen = models.ImageField(verbose_name='Adjunta una imagen', upload_to='empresa', blank=True, null=True, validators=[extensiones_validas])

    comentario = models.TextField( verbose_name="Comentarios", blank=True, null=True)



    class Meta:
        verbose_name = "Tabla de Escalación"
        verbose_name_plural = "Tablas de Escalaciones"

    def __str__(self):
        return self.empresa.name




class Guardia(models.Model):
    name  = models.CharField(max_length=200, verbose_name="Nombre", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="get_user", verbose_name="Usuario Asociado",
                             blank=True, null=True)

    escalacion = models.ForeignKey(TablaEscalacion, on_delete=models.CASCADE, related_name="get_escalacion",
                                verbose_name="Escalación", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Guardia"
        verbose_name_plural = "Guardias"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["name"]

    def __str__(self):
        return self.name

# Create your models here.







class GuardiaEspecialista(models.Model):
    guardia = models.ForeignKey(Guardia, on_delete=models.CASCADE, related_name="get_especialistas",
                              verbose_name="Seleccione el especialista", blank=True, null=True)

    imagen = models.ImageField(verbose_name='Adjunta una imagen', upload_to='empresa', blank=True, null=True,
                               validators=[extensiones_validas])

    fecha_inicio = models.DateField(verbose_name="Fecha Inicio", blank=True, null=True)
    fecha_fin = models.DateField(verbose_name="Fecha Fin", blank=True, null=True)

    comentario = models.TextField(verbose_name="Comentarios", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")


    class Meta:
        verbose_name = "Guardia por Especialista"
        verbose_name_plural = "Guardias por Especialistas"
        # Ordena de mas nuevo a mas antiguo
        ordering = ["-fecha_inicio",]

    def __str__(self):
        return str(self.guardia.name)