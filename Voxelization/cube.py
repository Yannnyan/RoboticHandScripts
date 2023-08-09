
# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import open3d as o3d
import os
from matplotlib import gridspec


def show_cube(path):
    voxel_grid = o3d.io.read_voxel_grid(path)
    # Create axis
    axes = [21, 21, 21]
    
    # Create Data
    data = np.zeros(axes)

    voxel_indices = [voxel.grid_index for voxel in voxel_grid.get_voxels()]
    for index in voxel_indices:
        data[tuple(index)] = 1
    # Control Transparency
    alpha = 0.9
    
    # Control colour
    colors = np.empty(axes + [4], dtype=np.float32)
    
    colors[:] = [1, 0, 0, alpha]  # red
    
    # Plot figure
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Voxels is used to customizations of the
    # sizes, positions and colors.
    ax.voxels(data, facecolors=colors)

    plt.show()

def show_cubes_differences(path1, path2, name='default'):
    voxel_grids = [o3d.io.read_voxel_grid(path1), o3d.io.read_voxel_grid(path2)]
    fig = plt.figure(figsize=(10,5))
    i = 221
    # create grid for different subplots
    # spec = gridspec.GridSpec(ncols=2, nrows=1,
    #                         width_ratios=[2, 1], wspace=0.5,
    #                         hspace=0.5, height_ratios=[1, 2])
    spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[6,6], wspace=0.5, hspace=0.5)

    for idx,voxel_grid in enumerate(voxel_grids):
        # Create axis
        axes = [21, 21, 21]
        
        # Create Data
        data = np.zeros(axes)

        voxel_indices = [voxel.grid_index for voxel in voxel_grid.get_voxels()]
        for index in voxel_indices:
            data[tuple(index)] = 1
        # Control Transparency
        alpha = 0.9
        
        # Control colour
        colors = np.empty(axes + [4], dtype=np.float32)
        
        colors[:] = [1, 0, 0, alpha]  # red
        

        ax = fig.add_subplot(spec[0, idx],projection='3d')
        ax.set_title(name + " With Algorithm" if idx == 0 else name + " Without Algorithm")
        ax.voxels(data, facecolors=colors)
    plt.show()

def write_cube_voxels(path, save_path):
    voxel_grid = o3d.io.read_voxel_grid(path)
    voxel_indices = np.array([voxel.grid_index for voxel in voxel_grid.get_voxels()])
    np.savetxt(save_path,voxel_indices)

def write_xyz_coords(cubes_dir, voxels_dir):
    for file in os.listdir(voxels_dir):
        write_cube_voxels(voxels_dir + "/" + file,
                        cubes_dir + "/" + "Cube_" + file.removeprefix('voxel_').removesuffix('.ply'))



def show_algorithm():
    
    files = os.listdir('voxels')


    for i in range(20):
        j = np.random.randint(0, len(files))
        name = 'voxels/' + files[j]
        show_cube(name)

def show_differences():
    dirname1 = 'temp_voxels'
    dirname2 = 'temp_voxels_noconv'

    lst = os.listdir(dirname1)

    for name in lst:
        path1 = dirname1 + "/" + name
        path2 = dirname2 + "/" + name
        show_cubes_differences(path1,path2,name.split("_")[2])

# show_differences()

# show_algorithm()


