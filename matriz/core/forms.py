from django import forms
from .models import GuardiaEspecialista



class GuardiaEspecialistaForm(forms.ModelForm):
    class Meta:
        model = GuardiaEspecialista
        fields = ['guardia', 'imagen','comentario','fecha_inicio','fecha_fin']
        widgets = {

            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'comentario': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 3, 'placeholder': 'Escriba algún comentario'}),
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder':'aaaa-mm-dd 00:00:00', 'required': 'True','type':'date'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder':'aaaa-mm-dd 00:00:00','required': 'True', 'type':'date'}),

        }

        labels = {
            'fecha_inicio': 'Fecha de Inicio',
        }
