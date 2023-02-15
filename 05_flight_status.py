# 这个代码使用droneKit连接无人机,给无人机一个向前1米每秒的速度，2秒。然后给一个向上飞行1米每秒的速度2秒。然后旋转偏航角90度
import time
from dronekit import connect, VehicleMode

# Connect to the vehicle.
vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Arm the vehicle and takeoff to a height of 10m
print("Arming motors")
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.simple_takeoff(10)
while True:
    if vehicle.location.global_relative_frame.alt >= 9.5:
        print("Vehicle has reached a target altitude of 10m")
        break
    time.sleep(1)

# Set the velocity to 1 m/s in the forward direction for 2 seconds
print("Setting airspeed to 1 m/s")
vehicle.airspeed = 1
vehicle.velocity = (1, 0, 0)
time.sleep(2)
vehicle.velocity = (0, 0, 0)

# Set the velocity to 1 m/s in the upward direction for 2 seconds
print("Setting climb rate to 1 m/s")
vehicle.velocity = (0, 0, -1)
time.sleep(2)
vehicle.velocity = (0, 0, 0)

# Rotate the vehicle's yaw by 90 degrees
print("Setting yaw to 90 degrees")
yaw = vehicle.attitude.yaw + 90
vehicle.simple_goto(vehicle.location.global_relative_frame, yaw=yaw)
time.sleep(2)

# Close vehicle object before exiting script
vehicle.close()
print("Vehicle disconnected")