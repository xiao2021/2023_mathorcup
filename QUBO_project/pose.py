import cv2
import numpy as np
from openpose import pyopenpose as op

# 加载OpenPose模型
params = dict()
params["model_folder"] = "openpose/models/"
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

# 定义要检测的姿态
POSE = [1, 2]  # 右手和左手举起

# 摄像头初始化
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # 读取一帧图像
    ret, frame = cap.read()

    # 姿态检测
    datum = op.Datum()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop([datum])
    keypoints = datum.poseKeypoints

    # 判断是否满足要求的姿态
    if len(keypoints.shape) > 0:
        pose = keypoints[:, POSE, 1]  # 取出要检测的关键点
        if np.all(pose[:, 1] < pose[0, 1] - 50):  # 判断手是否举起
            print("POSE DETECTED!")
            # 发送信号的代码放在这里

    # 显示检测结果
    cv2.imshow("OpenPose", datum.cvOutputData)

    # 按下q键退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
