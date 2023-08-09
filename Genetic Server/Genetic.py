import torch
import pygad
import pygad.torchga as torchga
import numpy as np
from HandBrain import HandBrain
from Dataset import HandDataset, CreateDataloder, CreateDatasets
import pickle

model = HandBrain()
train_dataloader = None
test_dataloader = None

class Genetic:
    def __init__(self, data_paths: dict):
        self.train, self.test = CreateDatasets(data_paths)
        self.train_dataloader = CreateDataloder(self.train)
        self.test_dataloader = CreateDataloder(self.test)

    def runGenetic(self, fitness_wrapper):
        torch_ga = torchga.TorchGA(model=model, num_solutions=100)
        num_generations = 50
        num_parents_mating = 10
        initial_population = torch_ga.population_weights
        ga_instance = pygad.GA(num_generations=num_generations,
                            num_parents_mating=num_parents_mating,
                            initial_population=initial_population,
                            fitness_func=fitness_wrapper,
                            save_best_solutions=True,
                            # save_solutions=True,
                            # parallel_processing=["thread" ,7],
                            crossover_type="two_points",
                            parent_selection_type="tournament",
                            mutation_probability=0.01,
                            mutation_type="random",
                            on_generation=lambda gen: print("Generation: ", gen.generations_completed),
                            on_crossover=lambda a,b : print("on crossover"),
                            on_fitness= lambda gen_instance,b: print("on fitness")
                            ,on_mutation=lambda a,b: print("on mutation"),
                            on_parents= lambda a,b: print("on parents")
                            ) 
        ga_instance.run()
        
        filename2 = "ga_instance2"
        ga_instance.save(filename2)
        print(ga_instance.summary())

        # filename = "ga_instance.pkl"
        # with open(filename, "wb") as f:
        #     pickle.dump(ga_instance, f)

    
    def GeneOutput(self, population):
        
        d = {}
        solution_ind = 0
        for solution in population:
            # get the weights dict 
            model_weights_dict = torchga.model_weights_as_dict(model=model,
                                                        weights_vector=solution)
            # load the weights dict onto a model
            model.load_state_dict(model_weights_dict)
            
            # load input values
            x = next(iter(self.train_dataloader))
            
            # outputs = []

            # for x1 in x:
            output = model(x).detach().cpu().numpy()
            # outputs.append(output)

            # stacked = np.vstack(outputs)

            output_lst = output.tolist()
            output_num = 0
            for output in output_lst:
                name = "gene_" + str(solution_ind)
                if name not in d:
                    d[name] = {}
                d[name]["object_" + str(output_num)] = output
                output_num += 1
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




