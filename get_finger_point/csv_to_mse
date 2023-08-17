import numpy as np
import pandas as pd
from get_finger_point import get_finger_point

def mse_sum(pred_points, actual_points):
    assert len(pred_points) == len(actual_points)

    return sum([(pred_points[i] - actual_points[i])**2 for i in len(pred_points)])

def main():
    predictions = pd.read_csv("predictions.csv")
    actuals = pd.read_csv("actuals.csv")

    assert len(predictions) == len(actuals)

    errors = []

    for i in range(len(predictions)):
        pred_joint_rotations = predictions.iloc[[i]].to_numpy()
        actual_joint_rotations = actuals.iloc[[i]].to_numpy()
        
        wrist_pred = pred_joint_rotations[0:3]
        thumb_pred = pred_joint_rotations[3:15]
        index_pred = pred_joint_rotations[15:24]
        middle_pred = pred_joint_rotations[24:33]
        ring_pred = pred_joint_rotations[33:42]
        pinky_pred = pred_joint_rotations[42:54]

        thumb_pred_point = get_finger_point(wrist_pred, np.array_split(thumb_pred, 3), "thumb")
        index_pred_point = get_finger_point(wrist_pred, np.array_split(index_pred, 3), "index")
        middle_pred_point = get_finger_point(wrist_pred, np.array_split(middle_pred, 3), "middle")
        ring_pred_point = get_finger_point(wrist_pred, np.array_split(ring_pred, 3), "ring")
        pinky_pred_point = get_finger_point(wrist_pred, np.array_split(pinky_pred, 3), "pinky")

        wrist_actual = actual_joint_rotations[0:3]
        thumb_actual = actual_joint_rotations[3:15]
        index_actual = actual_joint_rotations[15:24]
        middle_actual = actual_joint_rotations[24:33]
        ring_actual = actual_joint_rotations[33:42]
        pinky_actual = actual_joint_rotations[42:54]

        thumb_actual_point = get_finger_point(wrist_actual, np.array_split(thumb_actual, 3), "thumb")
        index_actual_point = get_finger_point(wrist_actual, np.array_split(index_actual, 3), "index")
        middle_actual_point = get_finger_point(wrist_actual, np.array_split(middle_actual, 3), "middle")
        ring_actual_point = get_finger_point(wrist_actual, np.array_split(ring_actual, 3), "ring")
        pinky_actual_point = get_finger_point(wrist_actual, np.array_split(pinky_actual, 3), "pinky")

        pred_points = [thumb_pred_point, index_pred_point, middle_pred_point, ring_pred_point, pinky_pred_point]
        actual_points = [thumb_actual_point, index_actual_point, middle_actual_point, ring_actual_point, pinky_actual_point]

        errors.append(mse_sum(pred_points, actual_points))


if __name__ == "__main__":
    main()