from get_finger_point import get_finger_points
from calculate_rotation_matrix import *
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
    a = df.to_numpy()[3][1:-1]
    positions = np.array_split(a[:54], 18)
    rotations = np.array_split(a[54:], 18)

    everything = np.array_split(a, 18+18)
    wrist_position = everything[17]

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

    # print(calculate_angles(tp[0], tp[1]))
    # print(thumb[0])

    # t_init = np.round([math.degrees(math.asin(tp[0][1]/vec_abs(tp[0]))), math.degrees(math.asin(tp[0][0]/vec_abs(tp[0]))), math.degrees(math.asin(tp[0][2]/vec_abs(tp[0])))], decimals=10)
    # i_init = np.round([math.degrees(math.asin(ip[0][1]/vec_abs(ip[0]))), math.degrees(math.asin(ip[0][0]/vec_abs(ip[0]))), math.degrees(math.asin(ip[0][2]/vec_abs(ip[0])))], decimals=10)
    # m_init = np.round([math.degrees(math.asin(mp[0][1]/vec_abs(mp[0]))), math.degrees(math.asin(mp[0][0]/vec_abs(mp[0]))), math.degrees(math.asin(mp[0][2]/vec_abs(mp[0])))], decimals=10)
    # r_init = np.round([math.degrees(math.asin(rp[0][1]/vec_abs(rp[0]))), math.degrees(math.asin(rp[0][0]/vec_abs(rp[0]))), math.degrees(math.asin(rp[0][2]/vec_abs(rp[0])))], decimals=10)
    # p_init = np.round([math.degrees(math.asin(pp[0][1]/vec_abs(pp[0]))), math.degrees(math.asin(pp[0][0]/vec_abs(pp[0]))), math.degrees(math.asin(pp[0][2]/vec_abs(pp[0])))], decimals=10)

    # for i in [t_init, i_init, m_init, r_init, p_init, "\n"]:
    #     print(i)

    Rwrist = R(wrist[0], wrist[1], wrist[2])
    t_wrist = Rwrist @ np.array(tp[0])
    i_wrist = Rwrist @ np.array(ip[0])
    m_wrist = Rwrist @ np.array(mp[0])
    r_wrist = Rwrist @ np.array(rp[0])
    p_wrist = Rwrist @ np.array(pp[0])

    t_init = calculate_init(t_wrist)
    i_init = calculate_init(i_wrist)
    m_init = calculate_init(m_wrist)
    r_init = calculate_init(r_wrist)
    p_init = calculate_init(p_wrist)

    for i in [t_init, i_init, m_init, r_init, p_init, "\n"]:
        print(i)

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

    # for ps in [[tp, tr], [ip, ir], [mp, mr], [rp, rr], [pp, pr]]:
    #     fig = plt.figure()
    #     ax = fig.add_subplot(projection='3d')
    #     for p in ps:
    #         ax.plot([0, p[0][0]], [0, p[0][1]], zs=[0, p[0][2]])
    #         for j in range(len(p)-1):
    #             ax.plot([p[j][0], p[j+1][0]], [p[j][1], p[j+1][1]], zs=[p[j][2], p[j+1][2]])
    #     # for j in range(len(ps[0])-1):
    #     #     print(math.dist(ps[0][j], ps[0][j+1]), end=", ")
    #     #     print(math.dist(ps[0][j], ps[0][j+1]))
    #     plt.show()



if __name__ == "__main__":
    main()