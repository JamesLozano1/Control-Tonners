# Generated by Django 5.0 on 2024-04-30 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0019_alter_toner_m_recargados_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='toner_m_recargados',
            name='fecha_entrega',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='toner_m_recargados',
            name='fecha_recibido',
            field=models.DateTimeField(null=True),
        ),
    ]
