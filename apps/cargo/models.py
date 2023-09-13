from django.db import models
from django.urls import reverse

# Create your models here.

class Cargo(models.Model):
    nome = models.CharField(max_length=60)
    classe = models.CharField(max_length=60)
    jornada = models.IntegerField()

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse("cargo_list")
    
    def __str__(self):
        return self.classe + ' - ' + self.nome
