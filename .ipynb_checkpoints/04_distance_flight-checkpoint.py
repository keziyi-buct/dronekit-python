# 这段代码使用droneKit连接无人机,控制无人机起飞到１０ｍ后，控制无人机向前飞行十米，随后向上飞行１ｍ，随后无人机返航

from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# 链接无人机
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# 飞行高度
altitude = 10

# 解锁无人机，起飞到指定高度
print("Arm and takeoff to %d meters." % altitude)
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.simple_takeoff(altitude)

# 等待起飞到指定高度
while True:
    if vehicle.location.global_relative_frame.alt >= altitude * 0.95:
        print("Reached target altitude")
        break
    time.sleep(1)

# 计算目标位置
target_location = LocationGlobalRelative(47.398001, 8.545592, altitude)

# 直线飞行到目标位置
print("Fly direct to target location")
vehicle.simple_goto(target_location)

# 等待飞行到目标位置
while True:
    distance = target_location.distance_to(vehicle.location.global_relative_frame)
    print("Distance to target: %s" % distance)
    if distance <= 1:
        print("Reached target")
        break
    time.sleep(1)

# 向上飞行一米
print("Climbing...")
vehicle.simple_goto(LocationGlobalRelative(vehicle.location.global_relative_frame.lat, vehicle.location.global_relative_frame.lon, vehicle.location.global_relative_frame.alt + 1))
time.sleep(5)

# 返航降落
print("Return to launch and land")
vehicle.mode = VehicleMode("RTL")
time.sleep(10)

# 关闭链接
vehicle.close()
