# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_categoria_codigo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diagnostico_set', to='catalogo.Diagnostico')),
            ],
            options={
                'verbose_name': 'Diagnostico',
                'verbose_name_plural': 'Diagnosticos',
            },
        ),
    ]
