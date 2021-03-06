# Generated by Django 3.2.6 on 2021-08-25 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome do Item')),
                ('pontos', models.PositiveIntegerField(verbose_name='Pontos')),
            ],
        ),
        migrations.CreateModel(
            name='Sobrevivente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, verbose_name='Nome do Sobrevivente')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=50, verbose_name='Sexo')),
                ('infectado', models.BooleanField(default=False, verbose_name='Infectado?')),
                ('latitude', models.CharField(max_length=200, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=200, null=True, verbose_name='Longitude')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Item')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sobrevivente.item', verbose_name='Item')),
                ('sobrevivente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sobrevivente.sobrevivente', verbose_name='Sobrevivente')),
            ],
        ),
    ]
