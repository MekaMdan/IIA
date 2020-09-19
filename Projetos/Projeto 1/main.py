from file_parser import parse_input_distance
from genetic_model import *

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

def fitness(percurso, distancias):
    cidade_origem = dicionario_indice_cidade['BsB']
    distancia_percorrida = 0
    for cidade_destino in percurso:
        distancia_percorrida += int(distancias[cidade_origem][cidade_destino])
        cidade_origem = cidade_destino
    cidade_destino = dicionario_indice_cidade['BsB']
    distancia_percorrida += int(distancias[cidade_origem][cidade_destino])
    return distancia_percorrida

def main():
    file_input_path = 'distancia_input.csv'
    distancias = parse_input_distance(file_input_path)

    geracao = criar_geracao()

    for individuo in geracao:
        print('individuo {} leva distância {}'.format(individuo, fitness(individuo,distancias)))

main()
