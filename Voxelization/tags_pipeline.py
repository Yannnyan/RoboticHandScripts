
import csv
from make_pcd import make_pcd_withConvex, make_pcd_noConvex
from voxel import saveAllVoxelsFromPCD
from cube import write_xyz_coords
import os

#convexes_path
# convex_wrist_path = r"C:\Users\Yan\Desktop\convexhull\convexhull.csv" # i.e mesh_wrist 
augment_wrist_path = r"C:\Users\Yan\Desktop\record.csv"
pcd_dir = 'temp_pcds_noconv'
voxel_dir = 'temp_voxels_noconv'
xyz_path = 'temp_cubes_noconv' # i.e cubes path

if not os.path.isdir(pcd_dir):
    os.mkdir(pcd_dir)
if not os.path.isdir(voxel_dir):
    os.mkdir(voxel_dir)
if not os.path.isdir(xyz_path):
    os.mkdir(xyz_path)

# make_pcd(convex_wrist_path, pcd_dir)

# make_pcd_withConvex(augment_wrist_path, pcd_dir)

make_pcd_noConvex(augment_wrist_path, pcd_dir)

saveAllVoxelsFromPCD(pcd_dir, voxel_dir)

write_xyz_coords(xyz_path, voxel_dir)







