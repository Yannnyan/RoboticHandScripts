import math
import numpy as np
def cos(angle):
    return math.cos(math.radians(angle))

def sin(angle):
    return math.sin(math.radians(angle))

def rotation_matrices(angle_x, angle_y, angle_z):
    x_rotation_matrix = np.array([1,0,0,
                              0, cos(angle_x), -sin(angle_x),
                              0, sin(angle_x), cos(angle_x)])
    
    y_rotation_matrix = np.array([cos(angle_y), 0, sin(angle_y),
                                0,1,0,
                                -sin(angle_y),0, cos(angle_y)])
    
    z_rotation_matrix = np.array([cos(angle_z), -sin(angle_z), 0,
                                sin(angle_z), cos(angle_z), 0,
                                0,0,1])
    x_rotation_matrix = x_rotation_matrix.reshape((3,3))
    y_rotation_matrix = y_rotation_matrix.reshape((3,3))
    z_rotation_matrix = z_rotation_matrix.reshape((3,3))
    return x_rotation_matrix, y_rotation_matrix, z_rotation_matrix


def rotate_vector(vector, angle_x, angle_y, angle_z):
    x_rotation_matrix, y_rotation_matrix, z_rotation_matrix = rotation_matrices(angle_x=angle_x, angle_y=angle_y, angle_z=angle_z)
    new_vector = vector @ x_rotation_matrix # rotate by x
    new_vector = new_vector @ y_rotation_matrix # rotate by y
    new_vector = new_vector @ z_rotation_matrix # rotate by z
    return new_vector



