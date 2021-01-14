from django.contrib import admin

from quiz_devpro.quiz.models import Pergunta, Aluno, Resposta


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'enunciado', 'disponivel']


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'criacao']


@admin.register(Resposta)
class RespostaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'pergunta', 'pontos', 'criacao']
