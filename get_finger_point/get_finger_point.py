import numpy as np
import math

def Rx(a):
    sin_a, cos_a = math.sin(a), math.cos(a)
    return np.array([
        [1, 0, 0],
        [0, cos_a, -sin_a],
        [0, sin_a, cos_a]
    ])

def Ry(a):
    sin_a, cos_a = math.sin(a), math.cos(a)
    return np.array([
        [cos_a, 0, sin_a],
        [0, 1, 0],
        [-sin_a, 0, cos_a]
    ])

def Rz(a):
    sin_a, cos_a = math.sin(a), math.cos(a)
    return np.array([
        [cos_a, -sin_a, 0],
        [sin_a, cos_a, 0],
        [0, 0, 1]
    ])

def R(a, b, c):
    return Rz(math.radians(a)) @ Ry(math.radians(b)) @ Rx(math.radians(c))

finger_to_distances = {"thumb":  [0.025718, 0.025138, 0.032887, 0.034182],
                       "index":  [0.100255, 0.038364, 0.024583, 0       ],
                       "middle": [0.096798, 0.043421, 0.027867, 0       ],
                       "ring":   [0.091677, 0.039445, 0.026879, 0       ],
                       "pinky":  [0.042660, 0.046176, 0.031074, 0.020545]}

def get_finger_point(wrist_rotation, joint_rotations, finger):

    a0, b0, c0 = wrist_rotation
    a1, b1, c1 = joint_rotations[0]
    a2, b2, c2 = joint_rotations[1]

    l1, l2, l3, l4 = finger_to_distances[finger]

    R0 = R(a0, b0, c0)
    R1 = R(a1, b1, c1)
    R2 = R(a2, b2, c2)

    p1_relative = np.array([l1, 0, 0]).T
    p1_effect = R0 @ p1_relative

    p2_relative = np.array([l2, 0, 0]).T
    p2_effect = R0 @ R1 @ p2_relative

    p3_relative = np.array([l3, 0, 0]).T
    p3_effect = R0 @ R1 @ R2 @ p3_relative

    if l4 == 0:
        p3 = p1_effect + p2_effect + p3_effect
        return np.round(p3, decimals=8)
    
    a3, b3, c3 = joint_rotations[2]
    R3 = R(a3, b3, c3)

    p4_relative = np.array([l4, 0, 0]).T
    p4_effect = R0 @ R1 @ R2 @ R3 @ p4_relative
    
    p4 = p1_effect + p2_effect + p3_effect + p4_effect

    return np.round(p4, decimals=8)

def get_finger_points(wrist_rotation, joint_rotations, finger):

    points = []

    a0, b0, c0 = wrist_rotation
    a1, b1, c1 = joint_rotations[0]
    a2, b2, c2 = joint_rotations[1]

    l1, l2, l3, l4 = finger_to_distances[finger]

    R0 = R(a0, b0, c0)
    R1 = R(a1, b1, c1)
    R2 = R(a2, b2, c2)

    p1_relative = np.array([l1, 0, 0]).T
    p1_effect = R0 @ p1_relative

    p2_relative = np.array([l2, 0, 0]).T
    p2_effect = R0 @ R1 @ p2_relative

    p3_relative = np.array([l3, 0, 0]).T
    p3_effect = R0 @ R1 @ R2 @ p3_relative

    p1 = p1_effect
    p2 = p1 + p2_effect
    p3 = p2 + p3_effect

    points.append(p1)
    points.append(p2)
    points.append(p3)

    if l4 == 0:
        return points
    
    a3, b3, c3 = joint_rotations[2]
    R3 = R(a3, b3, c3)

    p4_relative = np.array([l4, 0, 0]).T
    p4_effect = R0 @ R1 @ R2 @ R3 @ p4_relative
    
    p4 = p3 + p4_effect
    points.append(p4)

    return points

if __name__ == "__main__":
    wrist_rotation = np.array([310.3064, 225.4346, 56.68254])
    joint_rotations = np.array([
        [18.92999, 234.0272, 55.00048],
        [50.73119, 250.5061, 39.83798],
        [39.08791, 251.2982, 25.42211]
    ])
    print(get_finger_point(wrist_rotation, joint_rotations, "thumb"))