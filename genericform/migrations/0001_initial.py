# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 03:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('ordinal', models.IntegerField()),
                ('tipo', models.IntegerField(choices=[(1, b'NUMERICO'), (2, b'TEXTO'), (3, b'SELECCIONABLE_TEXTO')])),
                ('validation_dict', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GenericForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_corto', models.CharField(max_length=150)),
                ('mesa', models.IntegerField()),
                ('ordinal', models.IntegerField()),
                ('hora_entrega', models.TimeField()),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GenericOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('valor', models.CharField(help_text=b'El valor del campo sera convertido', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='GenericParentOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(1, b'NUMERICO'), (2, b'TEXTO'), (3, b'VERDADERO/FALSO')])),
                ('genericfield', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genericform.GenericField')),
            ],
        ),
        migrations.AddField(
            model_name='genericoption',
            name='genericparentoption',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genericform.GenericParentOption'),
        ),
        migrations.AddField(
            model_name='genericfield',
            name='genericform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='genericform.GenericForm'),
        ),
    ]