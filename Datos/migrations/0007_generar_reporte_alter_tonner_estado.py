# Generated by Django 5.0 on 2024-04-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0006_alter_tabla_t_toners_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Generar_Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='tonner',
            name='Estado',
            field=models.CharField(choices=[('Recargando', 'Recargando'), ('Disponible', 'Disponible'), ('En Uso', 'En Uso')], default='L', max_length=10),
        ),
    ]
