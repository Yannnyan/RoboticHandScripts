import matplotlib.pyplot as plt
# %matplotlib inline
import os
from matplotlib.pyplot import imread
from functools import reduce

import pygad


directory = r'outputs_images'  # Replace with the path to your directory

generations_lst = os.listdir(directory)

object_images = {}

object_names = []

generation_names = []

for gen_name in generations_lst:

    imgs_name_lst = os.listdir(os.path.join(directory, gen_name))
    
    generation_names.append(gen_name)
    
    tmp_lst = []

    for image_name in imgs_name_lst:
        
        object_name = image_name.split("_perspective")[0]
        if object_name not in object_images:
            
            object_images[object_name] = []

            object_names.append(object_name)


        image_path = os.path.join(directory, gen_name, image_name)
        
        image = imread(image_path)
        
        # object_images[object_name].append([image,gen_name])
        tmp_lst.append([image,gen_name, object_name])
    
    # pair together two images of the same generation and same object
    for object_name in object_names:
        filtered = list(filter(lambda x: x[2].startswith(object_name), tmp_lst))

        paired = [x[0] for x in filtered]

        paired.append(filtered[0][1])

        object_images[object_name].append(paired)



paired_object_images = object_images

# Assuming you have a list of image pairs called 'image_pairs'
# Each image pair contains two images (image1 and image2)


for j in range(2):
    fig, axes = plt.subplots(3, 5, figsize=(20, 10))

    index = 0
    row = 0
    for name in object_names:
        image_pairs = list(sorted(paired_object_images[name], key= lambda x: int(x[2].split("_")[1])))
        # print(len(image_pairs[1:]))
        axes = axes.flatten()
        
        for i, (image1, image2, generation_label) in enumerate(image_pairs[1:]):
            if i % 10 == 9:
                ax = axes[index]
                index += 1
                if j == 0:
                    ax.imshow(image2)
                    ax.axis('off')
                    ax.set_title(generation_label)
                else:
                    ax.imshow(image1)
                    ax.axis('off')
                    ax.set_title(generation_label)
        row += 1

    plt.tight_layout()
    plt.show()

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