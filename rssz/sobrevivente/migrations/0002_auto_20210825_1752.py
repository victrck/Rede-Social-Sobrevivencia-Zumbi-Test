# Generated by Django 3.2.6 on 2021-08-25 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sobrevivente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SinalizarContaminado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possivel_infectado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possivel_infectado', to='sobrevivente.sobrevivente')),
                ('sinalizado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sinalizado_por', to='sobrevivente.sobrevivente')),
            ],
        ),
        migrations.AddConstraint(
            model_name='sinalizarcontaminado',
            constraint=models.UniqueConstraint(fields=('sinalizado_por', 'possivel_infectado'), name='Restrição'),
        ),
    ]
