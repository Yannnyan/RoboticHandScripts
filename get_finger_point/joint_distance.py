import math
import numpy as np
from get_finger_point import Rx, Ry, Rz, finger_to_distances

def R(a, b, c):
    return Rz(math.radians(a)) @ Ry(math.radians(b)) @ Rx(math.radians(c))

p0 = np.array([-0.01384246, 0.01491809, 0.0157249])
a0, b0, c0 = 18.92999, 234.0272, 55.00048
a1, b1, c1 = 50.73119, 250.5061, 39.83798
a2, b2, c2 = 39.08791, 251.2982, 25.42211

l1, l2, l3, l4 = finger_to_distances["thumb"]

R0 = R(310.3064, 225.4346, 56.68254) @ R(a0, b0, c0)
R1 = R(a1, b1, c1)
R2 = R(a2, b2, c2)

p0 = np.array([-0.01384246, 0.01491809, 0.0157249])

p1_relative = np.array([l2, 0, 0]).T
p1_effect = R0 @ p1_relative

p2_relative = np.array([l3, 0, 0]).T
p2_effect = R0 @ R1 @ p2_relative

p3_relative = np.array([l4, 0, 0]).T
p3_effect = R0 @ R1 @ R2 @ p3_relative

p1 = p0 + p1_effect
p2 = p1 + p2_effect
p3 = p2 + p3_effect
print(np.round(p0, decimals=8))
print(np.round(p1, decimals=8))
print(np.round(p2, decimals=8))
print(np.round(p3, decimals=8))

# -0.01384246 0.01491809 0.0157249
# -0.02771854 0.03439689 0.02347043
# -0.05152154 0.04773235 0.04183289
# -0.07018429 0.05912209 0.06810883