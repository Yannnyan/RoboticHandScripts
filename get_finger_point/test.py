from get_finger_point import get_finger_points
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def draw_hand(w, t, i, m, r, p):

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for f in [t, i, m, r, p]:
        ax.plot([w[0], f[0][0]], [w[1], f[0][1]], zs=[w[2], f[0][2]])
        for j in range(len(f)-1):
            ax.plot([f[j][0], f[j+1][0]], [f[j][1], f[j+1][1]], zs=[f[j][2], f[j+1][2]])

    # for p in [w + t + i + m + r + p]:
    #     ax.scatter(p[0], p[1], p[2], marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()

def main():
    df = pd.read_csv("PositionBonesRight.csv")
    a = df.to_numpy()[0][1:-1]
    positions = np.array_split(a[:54], 18)
    rotations = np.array_split(a[54:], 18)

    w = positions[-1]
    t = positions[0:4]
    i = positions[4:7]
    m = positions[7:10]
    r = positions[10:13]
    p = positions[13:17]

    draw_hand(w, t, i, m, r, p)

    w = [0, 0, 0]
    t = get_finger_points(rotations[0], rotations[1:5], "thumb")
    i = get_finger_points(rotations[0], rotations[5:8], "index")
    m = get_finger_points(rotations[0], rotations[8:11], "middle")
    r = get_finger_points(rotations[0], rotations[11:14], "ring")
    p = get_finger_points(rotations[0], rotations[14:18], "pinky")

    draw_hand(w, t, i, m, r, p)


if __name__ == "__main__":
    main()