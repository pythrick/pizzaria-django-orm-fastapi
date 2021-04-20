from django.db import models


class TamanhoPizza(models.TextChoices):
    PEQUENA = "PEQUENA", "Pequena"
    MEDIA = "MEDIA", "Média"
    GRANDE = "GRANDE", "Grande"
    GIGANTE = "GIGANTE", "Gigante"


class Pizza(models.Model):
    sabor = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=10, choices=TamanhoPizza.choices)

    class Meta:
        db_table = "pizzas"
        verbose_name = "Pizza"
        verbose_name_plural = "Pizzas"

    def __str__(self):
        return self.sabor

    def __repr__(self):
        return f"{self.__class__.__name__}({self.sabor}, {self.tamanho})"
