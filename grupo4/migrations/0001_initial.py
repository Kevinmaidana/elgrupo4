# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Empleo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inicioContrato', models.DateField()),
                ('finContrato', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cuit', models.CharField(max_length=20)),
                ('razonSocial', models.CharField(max_length=30)),
                ('activa', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activa', models.BooleanField()),
                ('inicioContrato', models.DateField()),
                ('finContrato', models.DateField()),
                ('empresa', models.ForeignKey(to='grupo4.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dni', models.CharField(max_length=8)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fechaDeNacimiento', models.DateField()),
                ('desocupado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rubro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoDeTrabajo', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='tipoDeTrabajoQuePuedeRealizar',
            field=models.ForeignKey(to='grupo4.Rubro'),
        ),
        migrations.AddField(
            model_name='oferta',
            name='necesidad',
            field=models.ForeignKey(to='grupo4.Rubro'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='rubro',
            field=models.ForeignKey(to='grupo4.Rubro'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='empresa',
            field=models.ForeignKey(to='grupo4.Empresa'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='oferta',
            field=models.ForeignKey(to='grupo4.Oferta'),
        ),
        migrations.AddField(
            model_name='empleo',
            name='persona',
            field=models.ForeignKey(to='grupo4.Persona'),
        ),
    ]
