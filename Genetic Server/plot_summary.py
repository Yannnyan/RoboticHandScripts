import pygad


# filename = "ga_instance2"
filename = "ga_instance_simple"
ga_instance : pygad.GA = pygad.load(filename)

ga_instance.plot_fitness()
print(ga_instance.summary())

print("")
print("Best Solutions shape: ", "(" + str(len(ga_instance.best_solutions)) + ", " + str(len(ga_instance.best_solutions[0])) + ")")
print("")
print("")

print("Best Solutions : ", ga_instance.best_solutions)
print("")
print("")

print("Best Solutions fitness: ", ga_instance.best_solutions_fitness)