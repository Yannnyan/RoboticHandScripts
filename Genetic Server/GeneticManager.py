from Genetic import Genetic
from MessageManager import MessageManager 
from fastapi import FastAPI, Request, WebSocket
import asyncio
from threading import *
from ConcurencyManager import semaph_boss, finish_lst, tasks_lst
import GeneticSimple

msgManager = MessageManager()
genetic = None
feedback = None
iterations = -1

def initGenetic(msgPaths):
    global genetic
    # genetic = Genetic(msgPaths)
    genetic = GeneticSimple.GeneticSimple()


def initWebSocket(ws: WebSocket):
    global msgManager
    msgManager.initWebSocket(ws)

def fitness_wrapper(ga_instance, solution, index):
    """
    This function recieves 1d vector of weights i.e 54 neurons and an
    index to the solution from the population
    It should calculate the fitness score of the solution
    """
    global msgManager, genetic, semaph_boss, tasks_lst, finish_lst, feedback, iterations

    # evaluate entire population

    # for the first index we call to calculate the fitness scores for the whole population
    # if iterations < ga_instance.generations_completed:
    #     iterations = ga_instance.generations_completed
    #     population = ga_instance.population
        
    #     outputs = genetic.GeneOutput(population)
    #     print("[GeneticManager] appending msg")
    #     tasks_lst.put_nowait(outputs)
    #     print("[GeneticManager] acquire")
    #     semaph_boss.acquire(True)
    #     print("[GeneticManager] popping msg")
    #     rays_feedback = finish_lst.get_nowait()
    #     feedback = genetic.fitness_func_population(rays_feedback)
    
    #evaluate specific dna
    outputs = genetic.GeneOutput(solution)
    print("[GeneticManager] appending msg")
    tasks_lst.put_nowait(outputs)
    print("[GeneticManager] acquire")
    semaph_boss.acquire(True)
    print("[GeneticManager] popping msg")
    rays_feedback = finish_lst.get_nowait()

    return genetic.fitness_func([list(rays_feedback.values())[0]], index)

def run():
    # starting the genetic algorithm
    genetic.runGenetic(fitness_wrapper)








