# Generated by Django 5.0 on 2024-04-30 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0017_toner_m_recargados'),
    ]

    operations = [
        migrations.AddField(
            model_name='toner_m_recargados',
            name='estado',
            field=models.CharField(choices=[('HECHO', 'HECHO'), ('RECARGANDO', 'RECARGANDO')], default='RECARGANDO', max_length=10),
        ),
    ]
