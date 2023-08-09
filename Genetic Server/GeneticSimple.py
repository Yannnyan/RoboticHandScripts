
import torch
import pygad
import pygad.torchga as torchga
import numpy as np
from Dataset import HandDataset, CreateDataloder, CreateDatasets
import pickle
import Genetic


def custom_crossover(parents, size, ga_instance):
    # print(size)
    children = []
    # while len(children) < size[0]:
    num_parents = int((size[0] / 2)) + 1
    p1,p2 = np.random.randint(0,len(parents),size=(num_parents,)), np.random.randint(0,len(parents),size=(num_parents,))
    parent1, parent2 = parents[p1], parents[p2]
    
    child1 = parent1
    child2 = parent2
    choices = np.vstack([np.random.choice(18,size=(1,),replace=False) for _ in range(num_parents)])
    for choice in choices:
        for idx in choice:
            child1[idx: idx + 3] = parent2[idx: idx + 3]
            child2[idx: idx + 3] = parent1[idx: idx + 3]
    children = np.concatenate([child1,child2], axis=0)
    return children[:size[0]]

def custom_mutation(offsprings, ga_instance):
    # print(offsprings.shape)
    prop = ga_instance.mutation_probability
    for offspring in offsprings:
        for idx in range(len(offspring)):
            if np.random.random() <= prop:
                offspring[idx] += (np.random.random() - 0.5) * 2 * 0.125
    return offsprings

class GeneticSimple:
    def __init__(self):
        self.x  = 0

    def runGenetic(self, fitness_wrapper):
        num_generations = 2000
        num_parents_mating = 10
        num_genes = 54
        ga_instance = pygad.GA(num_generations=num_generations,
                            num_parents_mating=num_parents_mating,
                            num_genes=num_genes,
                            gene_type=float,
                            fitness_func=fitness_wrapper,
                            # save_best_solutions=True,
                            sol_per_pop=100,
                            # save_solutions=True,
                            # parallel_processing=["thread" ,7],
                            crossover_type=custom_crossover,
                            parent_selection_type="rws",
                            mutation_probability=0.01,
                            mutation_type = "random",
                            on_generation=lambda gen: print("Generation: ", gen.generations_completed),
                            on_crossover=lambda a,b : print("on crossover"),
                            on_fitness= lambda gen_instance,b: print("on fitness")
                            ,on_mutation=lambda a,b: print("on mutation"),
                            on_parents= lambda a,b: print("on parents")
                            )
        
        ga_instance.run()
        filename2 = "ga_instance_simple"
        ga_instance.save(filename2)
        print(ga_instance.summary())


    

    def GeneOutput(self, population):
        print("geneOutput")
        output_lst = torch.sigmoid(torch.tensor(population)).tolist()
        solution_ind = 0
        d = {}
        for output in output_lst:
            name = "gene_" + str(solution_ind)
            if name not in d:
                d[name] = {}
            d[name]["object_" + str(0)] = output
            solution_ind += 1
        return d

    def fitness_func(self,rays,index):
        """
        This function should recieve rays outputs as values
        of the distance from the fingers to the object to grab
        """

        ideal = torch.from_numpy(np.array([0,0,0,0,0]))
        loss_function = torch.nn.MSELoss()
        loss = loss_function(rays, ideal)
        eps =  0.00000001

        # we got minimization loss,
        # then we need to convert it to maximization loss
        # therefore we divide 1 by the loss + epsilon to avoid division by zero
        fitness_value = (1 / loss + eps)
        
        return fitness_value.item()

    def fitness_func_population(self, population_rays):
        """
        
        """
        d = {}
        for key in population_rays:
            index = key.split("_")[1]
            fitn = self.fitness_func(population_rays[key], index)
            d[index] = fitn
        lst = sorted(list(d.items()), key=lambda x: x[0])
        values = list(map(lambda x: x[1], lst))
        return values
    






