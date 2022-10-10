# Generated by Django 2.1.5 on 2022-09-12 19:08

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre de la Categoria')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_categoria', to='core.Categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Guardia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Guardia',
                'verbose_name_plural': 'Guardias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GuardiaEspecialista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='empresa', validators=[core.models.extensiones_validas], verbose_name='Adjunta una imagen')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha Inicio')),
                ('fecha_fin', models.DateField(blank=True, null=True, verbose_name='Fecha Fin')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentarios')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('guardia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_especialistas', to='core.Guardia', verbose_name='Seleccione el especialista')),
            ],
            options={
                'verbose_name': 'Guardia por Especialista',
                'verbose_name_plural': 'Guardias por Especialistas',
                'ordering': ['-fecha_inicio'],
            },
        ),
        migrations.CreateModel(
            name='TablaEscalacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel', models.FileField(blank=True, max_length=200, null=True, upload_to='documents', validators=[core.models.extensiones_validas_adjunto], verbose_name='Adjunta El documento')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='empresa', validators=[core.models.extensiones_validas], verbose_name='Adjunta una imagen')),
                ('comentario', models.TextField(blank=True, null=True, verbose_name='Comentarios')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_empresa', to='core.Empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Tabla de Escalación',
                'verbose_name_plural': 'Tablas de Escalaciones',
            },
        ),
        migrations.AddField(
            model_name='guardia',
            name='escalacion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_escalacion', to='core.TablaEscalacion', verbose_name='Escalación'),
        ),
        migrations.AddField(
            model_name='guardia',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_user', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Asociado'),
        ),
    ]
