import csv
from make_pcd import make_pcd_withConvex,make_one_pcd_withConvex
from voxel import saveAllVoxelsFromPCD, getVoxelFromPCD
from cube import write_xyz_coords
import open3d as o3d
import numpy as np


#convexes_path

def runPipeline(pcd_dir = 'pcds', voxel_dir = 'voxels', xyz_path = 'cubes', augment_wrist_path = r"C:\Users\Yan\Desktop\augment_input.csv"):

    # convex_wrist_path = r"C:\Users\Yan\Desktop\convexhull\convexhull.csv" # i.e mesh_wrist 
    
    
     # i.e cubes path

    # make_pcd(convex_wrist_path, pcd_dir)

    make_pcd_withConvex(augment_wrist_path, pcd_dir)

    saveAllVoxelsFromPCD(pcd_dir, voxel_dir)

    write_xyz_coords(xyz_path, voxel_dir)

def runPipelineShort(points, pcd_dir, voxel_dir):
    pcd_path = make_one_pcd_withConvex(points, pcd_dir=pcd_dir)

    voxel_path = pcd_path.removesuffix(".pcd") + ".ply"

    voxel_grid = getVoxelFromPCD(path=pcd_dir + pcd_path)

    voxel_indices = np.array([voxel.grid_index for voxel in voxel_grid.get_voxels()])

    return voxel_indices


# runPipeline()