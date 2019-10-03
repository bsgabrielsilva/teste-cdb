from django.db import models


class Arquivo(models.Model):
    titulo = models.CharField('Título', max_length=254, null=False)
    arquivo = models.FileField('Arquivo', upload_to='/', null=False)

    def __str__(self):
        return self.titulo
