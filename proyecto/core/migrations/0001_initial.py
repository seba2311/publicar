# Generated by Django 4.0.4 on 2022-06-10 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del usuario')),
                ('nombre_usuario', models.CharField(max_length=50, verbose_name='nombre usuario')),
                ('correo', models.CharField(max_length=50, verbose_name='correo')),
                ('clave', models.CharField(max_length=30, verbose_name='clave')),
                ('apellido', models.CharField(max_length=50, verbose_name='apellido')),
                ('comuna', models.CharField(max_length=50, verbose_name='comuna')),
            ],
        ),
    ]
