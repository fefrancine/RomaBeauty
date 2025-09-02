from django.db import models
from core.models import User


class Telefone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='telefone')
    telefone = models.CharField(max_length=20, default='000000000')

    def __str__(self):
        return f'{self.user.name} - {self.telefone}'
