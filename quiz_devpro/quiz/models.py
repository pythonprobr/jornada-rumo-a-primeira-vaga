from django.db import models


class Pergunta(models.Model):
    enunciado = models.TextField()
    alternativas= models.JSONField()
    disponivel= models.BooleanField(default=False)
    alternativa_correta=models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'),
    ])
