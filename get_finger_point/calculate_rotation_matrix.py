import numpy as np
from get_finger_point import R

def calculate_angles(point_a, point_b):
    Tx, Ty, Tz = np.array(point_b) - np.array(point_a)
    
    yaw = np.arctan2(Ty, Tx)    
    pitch = np.arctan2(-Tz, np.sqrt(Tx**2 + Ty**2))
    roll = np.arctan2(Ty, np.sqrt(Tx**2 + Tz**2))
    
    return [np.degrees(a) for a in [yaw, pitch, roll]]

def calculate_init(A):
    return calculate_angles([0, 0, 0], A)

def main():
    print(calculate_angles([-0.01384246, 0.01491809, 0.0157249], [-0.02771854, 0.03439689, 0.02347043]))
    Re1 = R(18.92999, 234.0272, 55.00048)
    print(calculate_angles([-0.01777315, 0.006033182, 0.01758263], [-0.03860189, 0.01605296, 0.02746838]))
    # 18.92999, 234.0272, 55.00048
    # 41.14223, 227.7031, 31.95643


if __name__ == "__main__":
    main()