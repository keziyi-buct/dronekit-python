#####这里我们展示droneKit连接无人机,控制无人机飞行到特定的三个地点，并自动返航

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
connection_string = "/dev/ttyACM0"  # 或者 "/dev/ttyUSB0"，根据无人机连接的串口进行设置
vehicle = connect(connection_string, wait_ready=True)
point1 = LocationGlobalRelative(37.793618, -122.397175, 20)  # 经度，纬度，高度（单位：米）
point2 = LocationGlobalRelative(37.793250, -122.398525, 20)
point3 = LocationGlobalRelative(37.794345, -122.398513, 20)

vehicle.simple_goto(point1)
while True:
    remaining_distance = point1.distance_to(vehicle.location.global_frame)
    if remaining_distance < 1:  # 当无人机与目标位置点的距离小于 1 米时，跳出循环
        break
    time.sleep(1)

vehicle.simple_goto(point2)
while True:
    remaining_distance = point2.distance_to(vehicle.location.global_frame)
    if remaining_distance < 1:
        break
    time.sleep(1)

vehicle.simple_goto(point3)
while True:
    remaining_distance = point3.distance_to(vehicle.location.global_frame)
    if remaining_distance < 1:
        break
    time.sleep(1)

vehicle.mode = VehicleMode("RTL")
while True:
    if not vehicle.armed:
        break
    time.sleep(1)

# 断开与无人机的连接
vehicle.close()
