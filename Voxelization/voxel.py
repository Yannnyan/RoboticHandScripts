import numpy as np
import open3d as o3d
import wget
import os

# url = 'https://raw.githubusercontent.com/PointCloudLibrary/pcl/master/test/bunny.pcd'
# #filename = wget.download(url)


def voxelizePCDTwoVisuals(path1,path2):
    pcd1 = o3d.io.read_point_cloud(path1)
    pcd2 = o3d.io.read_point_cloud(path2)
    print(pcd1,pcd2)

    print(type(pcd1),type(pcd2))

    N = 2000
    voxel_grids = []

    # pcd = pcd.(N)
    for pcd in [pcd1, pcd2]:

        # fit to unit cube
        pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
                center=pcd.get_center())
        pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
        # o3d.visualization.draw_geometries([pcd])

        print('voxelization')
        voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                                    voxel_size=0.05)        
        if pcd == pcd1:
            voxel_grid.translate([-3, 0,0])

        voxel_grids.append(voxel_grid)


    o3d.visualization.draw_geometries(voxel_grids)

def voxelizePCDVisual(path, name="open3d"):
    pcd = o3d.io.read_point_cloud(path)
    print(pcd)

    print(type(pcd))

    print('input')
    N = 2000
    # pcd = pcd.(N)
    # fit to unit cube
    pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
            center=pcd.get_center())
    pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(len(pcd.points), 3)))
    # o3d.visualization.draw_geometries([pcd], window_name=name)

    print('voxelization')
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                                voxel_size=0.05)
    # print(voxel_grid)
    # voxels = voxel_grid.get_voxels()
    # print(voxel_grid.get_axis_aligned_bounding_box())
    
    o3d.visualization.draw_geometries([voxel_grid], window_name=name)

def getVoxelFromPCD(path):
    pcd = o3d.io.read_point_cloud(path)

    # fit to unit cube
    pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
            center=pcd.get_center())
    # pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(len(pcd.points), 3)))

    # print('voxelization')
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                                voxel_size=0.05)
                                                                
    return voxel_grid

def saveVoxelFromPCD(path, save_path, verbose= True):
    pcd = o3d.io.read_point_cloud(path)
    if verbose:
        print(pcd, path, save_path)

    # fit to unit cube
    pcd.scale(1 / np.max(pcd.get_max_bound() - pcd.get_min_bound()),
            center=pcd.get_center())
    # pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(len(pcd.points), 3)))

    # print('voxelization')
    voxel_grid = o3d.geometry.VoxelGrid.create_from_point_cloud(pcd,
                                                                voxel_size=0.05)
                                                                
    o3d.io.write_voxel_grid(save_path, voxel_grid)

def saveAllVoxelsFromPCD(pcds_dir, voxel_dir):
    for file in os.listdir(pcds_dir):
        saveVoxelFromPCD(pcds_dir + "/" + file, voxel_dir + "/voxel_" + file.removeprefix("conv_").removesuffix(".pcd") + ".ply")


# def convert

# visualize voxels

# for i in range(10):
#     j = np.random.randint(0,999)
#     path = "pcds/conv" + str(j) + ".pcd"
#     voxelizePCDVisual(path)



# save voxels from pcd

# voxel_dir = 'voxels'
# pcds_dir = 'pcds'


# saveVoxelFromPCD(pcds_dir + "/conv1.pcd", "conv.ply")

# i = 0









