from django.db import models


class Sobrevivente(models.Model):

    opcoes_de_sexo = (('Masculino', 'Masculino'), ('Feminino', 'Feminino'))

    nome = models.CharField(
        verbose_name="Nome do Sobrevivente", max_length=200, blank=False, null=False)

    idade = models.IntegerField(verbose_name="Idade", blank=False, null=False)

    sexo = models.CharField(verbose_name="Sexo", max_length=50,
                            choices=opcoes_de_sexo, blank=False, null=False)

    infectado = models.BooleanField(verbose_name="Infectado?", default=False)

    latitude = models.CharField(
        verbose_name="Latitude", max_length=200, blank=False, null=True)

    longitude = models.CharField(
        verbose_name="Longitude", max_length=200, blank=False, null=True)

    def __str__(self):
        return self.nome


class Item(models.Model):

    nome = models.CharField(verbose_name="Nome do Item",
                            max_length=200, blank=False, null=False, unique=True)

    pontos = models.PositiveIntegerField(
        verbose_name="Pontos", blank=False, null=False)

    def __str__(self):
        return "Nome: " + self.nome + " - Pontos: " + str(self.pontos)


class Inventario(models.Model):

    sobrevivente = models.ForeignKey(Sobrevivente, verbose_name=(
        'Sobrevivente'), on_delete=models.CASCADE)

    item = models.ForeignKey(Item, verbose_name=(
        'Item'), on_delete=models.CASCADE)

    quantidade = models.PositiveIntegerField(('Quantidade'))

    def __str__(self):
        return self.sobrevivente.name
