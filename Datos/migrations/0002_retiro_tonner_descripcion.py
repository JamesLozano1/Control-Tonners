# Generated by Django 5.0 on 2024-06-22 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='retiro_tonner',
            name='descripcion',
            field=models.TextField(default='Sin descripción', max_length=500),
        ),
    ]
