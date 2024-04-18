# Generated by Django 5.0 on 2024-04-15 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tonner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cantidad', models.PositiveBigIntegerField()),
                ('N_Tonner', models.CharField(max_length=20)),
                ('Estado', models.CharField(choices=[('R', 'Recargando'), ('L', 'Libre'), ('O', 'Ocupado')], default='L', max_length=1)),
                ('imagen', models.ImageField(upload_to='tonner/')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('firma', models.ImageField(upload_to='firmas/')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Datos.area')),
            ],
        ),
        migrations.CreateModel(
            name='Retiro_Tonner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_retirada', models.PositiveIntegerField()),
                ('fecha_retiro', models.DateTimeField(auto_now_add=True)),
                ('r_persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Datos.persona')),
                ('r_tonner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Datos.tonner')),
            ],
        ),
    ]
