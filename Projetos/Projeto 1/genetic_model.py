import random

cidades_a_visitar = 9
tamanho_da_geracao = 10

def criar_individuo():
    individuo = []
    for i in range(cidades_a_visitar):
        nova_cidade = random.randrange(0,9)
        while(nova_cidade in individuo):
            nova_cidade = random.randrange(0,9)
        individuo.append(nova_cidade)
    return individuo

def criar_geracao():
    geracao = []
    for i in range(tamanho_da_geracao):
        geracao.append(criar_individuo())
    return geracao
