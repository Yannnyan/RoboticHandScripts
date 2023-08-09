from scipy.spatial import ConvexHull
from make_pcd import read_pcd, writePCD
from make_complete_conv import complete_convex
from voxel import saveVoxelFromPCD, voxelizePCDVisual, voxelizePCDTwoVisuals
import os
import numpy as np


def show_algorithm():

    for i in range(20):

        lst = os.listdir('pcds')

        j = np.random.randint(0, len(lst))
        
        init_pcd_path = "pcds/" + lst[j]

        new_pcd_path = "new_conv.pcd"

        new_voxel_path = "new_voxel.ply"

        old_voxel_path = "old_voxel.ply"

        conv = ConvexHull(read_pcd(init_pcd_path))

        more_points = complete_convex(conv)

        # write new voxels
        writePCD(more_points, new_pcd_path)

        saveVoxelFromPCD(new_pcd_path, new_voxel_path)
        
        #write old voxels
        saveVoxelFromPCD(init_pcd_path, old_voxel_path)

    # voxelizePCDVisual(new_voxel_path)
        # voxelizePCDTwoVisuals(new_voxel_path, old_voxel_path)
        voxelizePCDVisual(new_voxel_path, "new Voxels")
        voxelizePCDVisual(old_voxel_path, "Old voxels")


# show_algorithm()