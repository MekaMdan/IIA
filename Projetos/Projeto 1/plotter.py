# -*- coding: cp1252 -*-
import matplotlib.pyplot as plt

def plot_fitness(fitness):
    plt.plot(range(len(fitness)), fitness)
    plt.ylabel("Total distance")
    plt.xlabel("Generation")
    plt.show()

def plot_fitness_per_mutation(fitness):
    plt.plot(range(len(fitness)), fitness)
    plt.ylabel("Best fit")
    plt.xlabel("Number of mutations")
    plt.show()
