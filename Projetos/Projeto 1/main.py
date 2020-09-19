from file_parser import parse_input_distance
from plotter import plot_fitness, plot_fitness_per_mutation
from genetic_model import *


def traduzir_cromossomo(percurso):
    percurso_traduzido = ['BsB']
    for indice_da_cidade in percurso:
        percurso_traduzido.append(lista_de_cidades[indice_da_cidade])
    percurso_traduzido.append('BsB')
    return percurso_traduzido

def simulacao(numero_de_mutacoes, distancias, plot_results):
    numero_de_geracoes = 1000
    n_de_selecionados = 2
    

    geracao = criar_geracao()

    melhor_fitness_por_geracao = []

    for iteracao in range(numero_de_geracoes):

        fitness_resultados = []

        for individuo in geracao:
            fitness_resultados.append(fitness(individuo, distancias))
            
        individuos_selecionados = metodo_de_selecao(fitness_resultados,
                                                    n_de_selecionados,
                                                    geracao)

        melhor_fitness_por_geracao.append(min(fitness_resultados))

        melhor_individuo = geracao[fitness_resultados.index(min(fitness_resultados))]

        geracao = reproducao(individuos_selecionados[0], individuos_selecionados[1], numero_de_mutacoes)

    if(plot_results):
        print('Número de gerações da simulação: {}\n\n'.format(numero_de_geracoes))
        print('Resultados para  {} mutações:'.format(numero_de_mutacoes))
        print('Melhor fitness por geração:\n\t {}'.format(melhor_fitness_por_geracao))
        print('Melhor solução:\n\t {}'.format(traduzir_cromossomo(melhor_individuo)))
        print('Distância percorrida pela melhor solução: {}\n\n'.format(fitness(melhor_individuo, distancias)))

        plot_fitness(melhor_fitness_por_geracao)

        print('#######################################')

    return fitness(melhor_individuo, distancias), melhor_individuo

def main():
    print('Iniciando experimento...')
    file_input_path = 'distancia_input.csv'
    distancias = parse_input_distance(file_input_path)

    fitness_por_numero_de_mutacoes = []
    melhores_individuos = []
    for numero_de_mutacoes in range(25):
        fitness_do_melhor_individuo, melhor_individuo = simulacao(numero_de_mutacoes,
                                                        distancias,
                                                        False)
        fitness_por_numero_de_mutacoes.append(fitness_do_melhor_individuo)
        
        melhores_individuos.append(melhor_individuo)

    print('melhores fits por número de mutações: {}'.format(fitness_por_numero_de_mutacoes))
    numero_de_mutacoes_otimo = fitness_por_numero_de_mutacoes.index(min(fitness_por_numero_de_mutacoes))
    print('Melhor solução: \n\t {}\n\tCom {} mutações.\n\tCom distância total percorrida: {}'.format(traduzir_cromossomo(melhores_individuos[numero_de_mutacoes_otimo]),
                                                                                                     numero_de_mutacoes_otimo,
                                                                                                     fitness_por_numero_de_mutacoes[numero_de_mutacoes_otimo]))

    plot_fitness_per_mutation(fitness_por_numero_de_mutacoes)

    

main()
