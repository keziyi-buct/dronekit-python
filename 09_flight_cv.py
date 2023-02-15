#该代码通过DroneKit连接到无人机，控制飞机起飞到10米高度并保持高度不变。在此期间，使用OpenCV从树莓派上的摄像头获取图像，对其进行灰度转换、高斯模糊和边缘检测，最后找到轮廓并在原始图像帧中绘制轮廓。最后，通过按下“q”键来退出循环并降落飞机。
from dronekit import connect, VehicleMode, LocationGlobalRelative
import cv2
import numpy as np

# 设置连接地址和端口号
connection_string = '/dev/ttyACM0'

# 连接到飞行器
vehicle = connect(connection_string, baud=115200, wait_ready=True)

# 控制飞机起飞并悬停在当前位置
vehicle.mode = VehicleMode('GUIDED')
vehicle.armed = True
vehicle.simple_takeoff(10)
while not vehicle.location.global_relative_frame.alt >= 9.5:
    print("飞机正在起飞...")
    time.sleep(1)
print("飞机已经到达指定高度，开始图像处理！")

# 获取摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取图像帧
    ret, frame = cap.read()
    # 转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 应用高斯模糊以减少噪声
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)
    # 应用边缘检测以检测轮廓
    edges = cv2.Canny(blurred, 30, 150)
    # 找到轮廓
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 在原始帧中绘制轮廓
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    # 显示图像帧
    cv2.imshow('Frame', frame)
    # 如果按下“q”键，则退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 清理并退出
cap.release()
cv2.destroyAllWindows()
vehicle.mode = VehicleMode('LAND')
vehicle.armed = False
vehicle.close()
