from django.utils import timezone
from django.db import models

from account.models import CustomUser
from apps.cargo.models import Cargo
from apps.orgao.models import Orgao


class Vinculo(models.Model):
    servidor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    matricula = models.IntegerField(null=True)
    lotacao = models.ForeignKey(Orgao, on_delete=models.CASCADE, null=False)
    data_inicio = models.DateField(default=timezone.now)
    data_fim = models.DateField(blank=True, null=True)
    data_inclusao = models.DateTimeField(default=timezone.now)
    data_alteracao = models.DateTimeField(blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    situacao = models.BooleanField(default=True)

    def modify(self):
        self.data_alteracao = timezone.now()
        self.save()