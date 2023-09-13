from django.db import models
import uuid
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Documento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    codigo = models.IntegerField()
    descricao = models.CharField(max_length=60)
    utiliza_num_ano = models.BooleanField()
    createdAt = models.DateTimeField(default=timezone.now)
    createdBy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='documentos_criados')
    modifyAt = models.DateTimeField(blank=True, null=True)
    modifyBy = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='documentos_modificados', default=None, null=True)

    def modify(self):
        self.modifyAt = timezone.now()
        self.modifyBy = settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        self.save()

    def __str__(self):
        return self.codigo
