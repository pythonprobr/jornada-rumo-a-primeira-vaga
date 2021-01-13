from django.http import HttpResponse
from django.shortcuts import render

from quiz_devpro.quiz.models import Pergunta


def indice(requisicao):
    return render(requisicao, 'quiz/indice.html')


def perguntas(requisicao, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    contexto = {'indice': indice, 'pergunta': pergunta}
    return render(requisicao, 'quiz/pergunta.html', contexto)


def classificacao(requisicao):
    return render(requisicao, 'quiz/classificacao.html')
