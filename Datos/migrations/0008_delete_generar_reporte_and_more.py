# Generated by Django 5.0 on 2024-04-23 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0007_generar_reporte_alter_tonner_estado'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Generar_Reporte',
        ),
        migrations.RenameField(
            model_name='tabla_t_toners',
            old_name='n_impresoras',
            new_name='numero_impresoras',
        ),
    ]