# Generated by Django 3.2.8 on 2021-12-08 02:15

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                 parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('foto', models.ImageField(blank=True, null=True,
                 upload_to='perfiles', verbose_name='Foto de Perfil')),
                ('password2', models.CharField(default='',
                 max_length=62, verbose_name='Verfica tu contraseña')),
                ('puede_vender', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Vendedor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE,
                 parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('foto_perfil', models.ImageField(blank=True, null=True,
                 upload_to='perfil', verbose_name='Foto de Perfil')),
                ('direccion', models.CharField(default='',
                 max_length=255, verbose_name='Direccion')),
                ('telefono', models.CharField(default='',
                 max_length=10, verbose_name='Telefono')),
                ('password_rev', models.CharField(default='',
                 max_length=62, verbose_name='Verifica tu contraseña')),
                ('descripcion', models.CharField(blank=True,
                 max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                 to='usuarios.estado', verbose_name='Estado')),
            ],
        ),
    ]
