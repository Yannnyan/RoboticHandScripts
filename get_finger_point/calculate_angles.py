import numpy as np

def calculate_angles(point_a, point_b):
    Tx, Ty, Tz = np.array(point_b) - np.array(point_a)
    
    yaw = np.arctan2(Ty, Tx)    
    pitch = np.arctan2(-Tz, np.sqrt(Tx**2 + Ty**2))
    roll = np.arctan2(Ty, np.sqrt(Tx**2 + Tz**2))
    
    return [np.degrees(a) for a in [yaw, pitch, roll]]

def calculate_init(A):
    return calculate_angles([0, 0, 0], A)