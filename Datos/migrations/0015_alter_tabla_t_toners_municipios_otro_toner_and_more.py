# Generated by Django 5.0 on 2024-04-25 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Datos', '0014_alter_tabla_t_toners_municipios_comprobado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabla_t_toners_municipios',
            name='otro_toner',
            field=models.CharField(choices=[('105A', '105A'), ('30A', '30A'), ('83A', '83A'), ('136A', '136A'), ('175A', '175A'), ('17A', '17A'), ('19A', '19A'), ('85A', '85A'), ('226A', '226A'), ('D1015', 'D1015'), ('MLT-D1018', 'MLT-D1018'), ('101S', '101S'), ('TINTA', 'TINTA'), ('N/A', 'N/A')], default='N/A', max_length=9),
        ),
        migrations.AlterField(
            model_name='tabla_t_toners_municipios',
            name='toner_de_impresora',
            field=models.CharField(choices=[('105A', '105A'), ('30A', '30A'), ('83A', '83A'), ('136A', '136A'), ('175A', '175A'), ('17A', '17A'), ('19A', '19A'), ('85A', '85A'), ('226A', '226A'), ('D1015', 'D1015'), ('MLT-D1018', 'MLT-D1018'), ('101S', '101S'), ('TINTA', 'TINTA'), ('N/A', 'N/A')], default='N/A', max_length=9),
        ),
        migrations.DeleteModel(
            name='Toner_Recarga',
        ),
    ]
