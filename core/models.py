from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class diaoperadores(models.Model):
    id = models.AutoField(primary_key=True),
    operador = models.CharField(max_length=50, null=False),
    item = models.CharField(max_length=50, null=False),
    dia = models.DateTimeField(verbose_name='Data da producao', null=False),
    quantidade = models.IntegerField(10),
    rejeicoes = models.IntegerField(10),
    aprovado = models.IntegerField(10),
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table: 'diaoperadores'
