import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
from PointsChanger import Changer
import plotly.figure_factory as ff
import sys
sys.path.append(r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Voxelization")
from make_pcd import read_pcd
import os
from matplotlib import gridspec, cm
import numpy as np
from mayavi import mlab
from tvtk.pyface.light_manager import CameraLight

def show_comparison_matplotlib(points_changed, points_conv, conv_hull, name, object_name, save_path):

    fig = plt.figure(figsize=(12,5))
    plt.axis('off')
    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 20,
        }
    plt.suptitle(name,size=20)

    fig.tight_layout(pad=2)
    
    spec = gridspec.GridSpec(ncols=2, nrows=1, width_ratios=[4,4], height_ratios=[5], wspace=0.1, hspace=0.5)

    # spec = gridspec.GridSpec(ncols=3, nrows=1, width_ratios=[4,4,4], height_ratios=[5], wspace=0.1, hspace=0.5)
    
    # plt.text(0.62,-0.03,object_name, fontsize=13, bbox=dict(facecolor='white', alpha=0.5))
    plt.text(0.42, 0, object_name, fontsize =13, bbox=dict(facecolor='white', alpha=0.5))

    # ax = fig.add_subplot(spec[0, 2],projection='3d')
    # ax.title.set_text("Trisurf of the convex simplices")
    # ax.plot_trisurf(conv_hull.points[:,0],
    #                 conv_hull.points[:,1],
    #                 conv_hull.points[:,2], triangles=conv_hull.simplices)
    # ax.title.set_size(16)

    points_arr = [points_changed, points_conv]


    for ind, points in enumerate(points_arr):
        if ind == 1:
            ax = fig.add_subplot(spec[0, ind],projection='3d')
            ax.title.set_text(str(len(points_changed)) + " Points After Algorithm" if ind == 0 else str(len(points_conv)) + " Points Before Algorithm")
            ax.plot_trisurf(conv_hull.points[:,0],
                            conv_hull.points[:,1],
                            conv_hull.points[:,2], triangles=conv_hull.simplices)
            continue
        ax = fig.add_subplot(spec[0, ind],projection='3d')
        ax.set_title(str(len(points_changed)) + " Points After Algorithm" if ind == 0 else str(len(points_conv)) + " Points Before Algorithm")
        # ax.title.set_position([.5,0.5])
        # if ind == 0:

        ax.scatter3D(points[:,0],points[:,1],points[:,2],c='blue')
        ax.title.set_size(16)


    plt.savefig(save_path)
    # plt.show()


def show_comparison_mayavi(points_changed, points_conv, conv_hull, name, object_name, save_path):
    # s = mlab.test_plot3d()
    # Create a sphere mesh
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 30)
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

    # Plot the sphere
    mesh = mlab.mesh(x, y, z, color=(0.6, 0.6, 1))  # Sphere color is light blue

    # Add lighting to the scene
    light = mlab.points3d(0, 0, 0, scale_factor=1, color=(1, 1, 1))
    light.actor.property.lighting = True
    # light.actor.light_type = 'vtkLightKit'
    light.actor.light_kit = 'vtkLightKitKeyLight'
    light.actor.light_kit.intensity = 0.5

    mlab.show()


def showResults():

    # dirname = r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Voxelization\temp_pcds_noconv"

    dirname = r"C:\Users\Yan\Desktop\Robotic hand\Scripts\Voxelization\temp_pcds"

    save_dirname = r"C:\Users\Yan\Desktop\Robotic hand\pictures\ConvexHull Algorithm Comparison\V4"

    if not os.path.isdir(save_dirname):
        os.mkdir(save_dirname)

    changer = Changer()

    lst = os.listdir(dirname)

    for file in lst:
        points = read_pcd(dirname + "\\" + file)

        conv = ConvexHull(points)

        # conv_points = conv.points[conv.vertices]

        conv_points = np.array(points)

        num_points = len(conv_points)

        changed_points = changer.changePoints(np.array(conv_points), 2000)

        object_name = file.split("_")[2]

        # show_comparison_matplotlib(changed_points, conv_points, conv ,"After VS Before Point Amount Fixation Alg" , "Object: " + object_name, save_dirname + "\\" + object_name + ".png")
        
        show_comparison_mayavi(changed_points, conv_points, conv ,"After VS Before Point Amount Fixation Alg" , "Object: " + object_name, save_dirname + "\\" + object_name + ".png")


# showResults()