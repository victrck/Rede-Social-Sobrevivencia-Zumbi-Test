# Generated by Django 3.2.6 on 2021-08-26 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobrevivente', '0003_remove_sinalizarcontaminado_restrição'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='quantidade',
            field=models.PositiveIntegerField(verbose_name='Quantidade'),
        ),
    ]
