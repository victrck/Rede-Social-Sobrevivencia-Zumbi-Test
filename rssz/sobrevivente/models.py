from django.db import models


class Ultimolocal(models.Model):

    latitude = models.CharField(
        verbose_name="Latitude",
        max_length=200,
        blank=False,
        null=False
    )

    longitude = models.CharField(
        verbose_name="Longitude",
        max_length=200,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.latitude + " - " + self.longitude


class Sobrevivente(models.Model):

    opcoes_de_sexo = (
        ('Masculino', 'Masculino'),
        ('Feminino', 'Feminino')
    )

    nome = models.CharField(
        verbose_name="Nome do Sobrevivente",
        max_length=200,
        blank=False,
        null=False
    )

    idade = models.IntegerField(
        verbose_name="Idade",
        blank=False,
        null=False
    )

    sexo = models.CharField(
        verbose_name="Sexo",
        max_length=50,
        choices=opcoes_de_sexo,
        blank=False,
        null=False
    )

    infectado = models.BooleanField(
        verbose_name="Infectado?",
        default=False
    )

    ultimo_local = models.ForeignKey(
        Ultimolocal,
        on_delete=models.CASCADE,
        related_name='ultimo_local',
        null=False,
        blank=False
    )

    def __str__(self):
        return self.nome
