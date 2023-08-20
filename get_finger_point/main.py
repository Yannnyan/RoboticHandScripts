from get_finger_point import get_finger_points
from calculate_angles import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def draw_hand(t, i, m, r, p):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for f in [t, i, m, r, p]:
        ax.plot([0, f[0][0]], [0, f[0][1]], [0, f[0][2]])
        for j in range(len(f)-1):
            ax.plot([f[j][0], f[j+1][0]], [f[j][1], f[j+1][1]], [f[j][2], f[j+1][2]])

    for f in [[[0, 0, 0,]], t, i, m, r, p]:
        for p in f:
            ax.scatter(p[0], p[1], p[2], marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

def vec_abs(vec):
    return math.sqrt(vec[0]**2 + vec[1]**2 + vec[2]**2)

def main():
    df = pd.read_csv("PositionBonesRight.csv")
    a = df.to_numpy()[0][1:-1]
    positions = np.array_split(a[:54], 18)
    rotations = np.array_split(a[54:], 18)

    wrist = rotations[0]
    thumb = rotations[1:5]
    index = rotations[5:8]
    middle = rotations[8:11]
    ring = rotations[11:14]
    pinky = rotations[14:18]

    tp = positions[0:4]
    ip = positions[4:7]
    mp = positions[7:10]
    rp = positions[10:13]
    pp = positions[13:17]

    draw_hand(tp, ip, mp, rp, pp)

    tr = get_finger_points(wrist, thumb, "thumb")
    ir = get_finger_points(wrist, index, "index")
    mr = get_finger_points(wrist, middle, "middle")
    rr = get_finger_points(wrist, ring, "ring")
    pr = get_finger_points(wrist, pinky, "pinky")

    draw_hand(tr, ir, mr, rr, pr)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for f in [tp, ip, mp, rp, pp, tr, ir, mr, rr, pr]:
        ax.plot([0, f[0][0]], [0, f[0][1]], [0, f[0][2]])

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


if __name__ == "__main__":
    main()