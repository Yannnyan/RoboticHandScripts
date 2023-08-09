[33mcommit 70f6e40fa70561733068748136bed6e0a67b84e0[m[33m ([m[1;36mHEAD -> [m[1;32mmain[m[33m)[m
Author: Yan <regoner2@gmail.com>
Date:   Tue Aug 8 02:23:58 2023 +0300

    gitignore mod

[1mdiff --git a/.gitignore b/.gitignore[m
[1mindex b432f71..ab51361 100644[m
[1m--- a/.gitignore[m
[1m+++ b/.gitignore[m
[36m@@ -8,11 +8,11 @@[m [mcubes/[m
 [m
 temp_cubes/[m
 [m
[31m-temp_cubes_nonconv/[m
[32m+[m[32mtemp_cubes_noconv/[m
 [m
 temp_pcds/[m
 [m
[31m-temp_pcds_nonconv/[m
[32m+[m[32mtemp_pcds_noconv/[m
 [m
 temp_voxels/[m
 [m
[1mdiff --git a/Voxelization/__pycache__/cube.cpython-310.pyc b/Voxelization/__pycache__/cube.cpython-310.pyc[m
[1mindex 37a005c..b31f7f2 100644[m
Binary files a/Voxelization/__pycache__/cube.cpython-310.pyc and b/Voxelization/__pycache__/cube.cpython-310.pyc differ
[1mdiff --git a/Voxelization/__pycache__/make_pcd.cpython-310.pyc b/Voxelization/__pycache__/make_pcd.cpython-310.pyc[m
[1mindex af7c201..b19274b 100644[m
Binary files a/Voxelization/__pycache__/make_pcd.cpython-310.pyc and b/Voxelization/__pycache__/make_pcd.cpython-310.pyc differ
[1mdiff --git a/Voxelization/cube.py b/Voxelization/cube.py[m
[1mindex e8ad8c7..2a520f7 100644[m
[1m--- a/Voxelization/cube.py[m
[1m+++ b/Voxelization/cube.py[m
[36m@@ -104,7 +104,7 @@[m [mdef show_differences():[m
         path2 = dirname2 + "/" + name[m
         show_cubes_differences(path1,path2,name.split("_")[2])[m
 [m
[31m-show_differences()[m
[32m+[m[32m# show_differences()[m
 [m
 # show_algorithm()[m
 [m
[1mdiff --git a/Voxelization/tags_pipeline.py b/Voxelization/tags_pipeline.py[m
[1mindex b30af4e..45f7544 100644[m
[1m--- a/Voxelization/tags_pipeline.py[m
[1m+++ b/Voxelization/tags_pipeline.py[m
[36m@@ -5,7 +5,6 @@[m [mfrom voxel import saveAllVoxelsFromPCD[m
 from cube import write_xyz_coords[m
 import os[m
 [m
[31m-[m
 #convexes_path[m
 # convex_wrist_path = r"C:\Users\Yan\Desktop\convexhull\convexhull.csv" # i.e mesh_wrist [m
 augment_wrist_path = r"C:\Users\Yan\Desktop\record.csv"[m
[36m@@ -13,10 +12,12 @@[m [mpcd_dir = 'temp_pcds_noconv'[m
 voxel_dir = 'temp_voxels_noconv'[m
 xyz_path = 'temp_cubes_noconv' # i.e cubes path[m
 [m
[31m-[m
[31m-os.mkdir(pcd_dir)[m
[31m-os.mkdir(voxel_dir)[m
[31m-os.mkdir(xyz_path)[m
[32m+[m[32mif not os.path.isdir(pcd_dir):[m
[32m+[m[32m    os.mkdir(pcd_dir)[m
[32m+[m[32mif not os.path.isdir(voxel_dir):[m
[32m+[m[32m    os.mkdir(voxel_dir)[m
[32m+[m[32mif not os.path.isdir(xyz_path):[m
[32m+[m[32m    os.mkdir(xyz_path)[m
 [m
 # make_pcd(convex_wrist_path, pcd_dir)[m
 [m
