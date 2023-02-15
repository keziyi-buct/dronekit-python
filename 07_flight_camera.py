#使用droneKit连接无人机,并控制摄像头转动，读取摄像头视频30s并保存下来
from dronekit import connect, VehicleMode
import time

# 连接无人机
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)

# 控制摄像头转动
vehicle.gimbal.rotate(30, 0, 0)

# 等待一段时间
time.sleep(5)

# 停止摄像头转动
vehicle.gimbal.rotate(0, 0, 0)

# 断开与无人机的连接
vehicle.close()

import cv2

# 定义视频捕获对象
cap = cv2.VideoCapture('tcp://127.0.0.1:8080')

# 定义视频编码器和写入对象
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# 读取并保存视频
start_time = time.time()
while(cap.isOpened() and time.time() - start_time < 30):
    ret, frame = cap.read()
    if ret:
        out.write(frame)
    else:
        break

# 释放视频捕获对象和写入对象
cap.release()
out.release()
