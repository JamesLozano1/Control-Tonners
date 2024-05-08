# Generated by Django 5.0 on 2024-04-30 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0016_recargar_toner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toner_M_Recargados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField()),
                ('toner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Datos.tonner')),
            ],
        ),
    ]