import random

cidades_a_visitar = 9
tamanho_da_geracao = 10

dicionario_indice_cidade = {
    'SP': 0,
    'BA': 1,
    'RJ': 2,
    'Lima': 3,
    'Bog': 4,
    'Sant': 5,
    'Carac': 6,
    'BH': 7,
    'PoA': 8,
    'BsB': 9
    }


lista_de_cidades = ['SP',
                    'BA',
                    'RJ',
                    'Lima',
                    'Bog',
                    'Sant',
                    'Carac',
                    'BH',
                    'PoA',
                    'BsB']

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

def fitness(percurso, distancias):
    cidade_origem = dicionario_indice_cidade['BsB']
    distancia_percorrida = 0
    for cidade_destino in percurso:
        distancia_percorrida += int(distancias[cidade_origem][cidade_destino])
        cidade_origem = cidade_destino
    cidade_destino = dicionario_indice_cidade['BsB']
    distancia_percorrida += int(distancias[cidade_origem][cidade_destino])
    return distancia_percorrida

def metodo_de_selecao(fitness_resultados, numero_de_selecionados, geracao):
    individuos_selecionados = geracao[:]
    fitness_selecionados = fitness_resultados[:]

    for iteracao in range(len(geracao) - numero_de_selecionados):
        indice_a_remover = fitness_selecionados.index(max(fitness_selecionados))
        individuos_selecionados.pop(indice_a_remover)
        fitness_selecionados.pop(indice_a_remover)

    return individuos_selecionados

def find_duplicate(lista):
    aparicao_de_elementos = [0] * cidades_a_visitar
    for element in lista:
        aparicao_de_elementos[element] += 1
    if (max(aparicao_de_elementos) == 1):
        return None
    return aparicao_de_elementos.index(max(aparicao_de_elementos))

def find_indexes_by_value(lista, value):
    indexes = []
    for index in range(len(lista)):
        if (lista[index] == value):
            indexes.append(index)
    return indexes

def find_missing_element(cromossomo):
    for city in range(cidades_a_visitar):
        if (city not in cromossomo):
            return city

def crossover_correction(cromossomo):
    cidade_duplicada = find_duplicate(cromossomo)
    while (cidade_duplicada != None):
        indexes = find_indexes_by_value(cromossomo, cidade_duplicada)
        random_index_to_change = indexes[random.randrange(0, len(indexes))]
        cromossomo[random_index_to_change] = find_missing_element(cromossomo)
        cidade_duplicada = find_duplicate(cromossomo)
    return cromossomo

def mutation(cromossomo, number_of_permutations):
    cromossomo_corrigido = crossover_correction(cromossomo)
    for permutation in range(number_of_permutations):
        random_index = random.randrange(0,9)
        random_second_index = random.randrange(0,9)
        while(random_index == random_second_index):
            random_second_index = random.randrange(0,9)
        aux = cromossomo_corrigido[random_index]
        cromossomo_corrigido[random_index] = cromossomo_corrigido[random_second_index]
        cromossomo_corrigido[random_second_index] = aux
    return cromossomo_corrigido

def crossing_over(pai, mae, numero_de_mutacoes):
    filhos = []
    crossoverpoint = random.randrange(1, len(pai) - 1)
    filhos.append(mutation(pai[:crossoverpoint] + mae[crossoverpoint:], numero_de_mutacoes))
    filhos.append(mutation(pai[crossoverpoint:] + mae[:crossoverpoint], numero_de_mutacoes))
    filhos.append(mutation(mae[:crossoverpoint] + pai[crossoverpoint:], numero_de_mutacoes))
    filhos.append(mutation(mae[crossoverpoint:] + pai[:crossoverpoint], numero_de_mutacoes))
    return filhos

def reproducao(pai, mae, numero_de_mutacoes):
    nova_geracao = [pai, mae]
    nova_geracao += crossing_over(pai, mae, numero_de_mutacoes)
    nova_geracao += crossing_over(pai, mae, numero_de_mutacoes)
    return nova_geracao
