# Biblioteca de classificação utilizada: https://pypi.org/project/Bayesian/0.3.1/

from bayesian import classify, classify_file, classify_normal
from knowledge_base import *
from input_reader import symptoms


def train_classifiers():
    avaliation = symptoms()
    diagnosis = classify_normal(avaliation,
                                knowledge_base())

    print("A doença provável é:", diagnosis)


def main():
    print("Olá! Por favor, informe os seus sintomas:")
    train_classifiers()


main()
