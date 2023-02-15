import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

#通过SITL仿真运行
print('Connecting...')
vehicle = connect('udp:127.0.0.1:14551')

#设置飞行速度5m/s
gnd_speed = 5 # [m/s]

#定义起飞函数
def arm_and_takeoff(altitude):

   while not vehicle.is_armable:
      print("waiting to be armable")
      time.sleep(1)

   print("Arming motors")
   vehicle.mode = VehicleMode("GUIDED")
   vehicle.armed = True

   while not vehicle.armed: time.sleep(1)

   print("Taking Off")
   vehicle.simple_takeoff(altitude)

   while True:
      v_alt = vehicle.location.global_relative_frame.alt
      print(">> Altitude = %.1f m"%v_alt)
      if v_alt >= altitude * 0.95:
          print("Target altitude reached")
          break
      time.sleep(1)

#定义发送mavlink速度命令的功能
def set_velocity_body(vehicle, vx, vy, vz):
    """ Remember: vz is positive downward!!! 
    
    Bitmask to indicate which dimensions should be ignored by the vehicle 
    (a value of 0b0000000000000000 or 0b0000001000000000 indicates that 
    none of the setpoint dimensions should be ignored). Mapping: 
    bit 1: x,  bit 2: y,  bit 3: z, 
    bit 4: vx, bit 5: vy, bit 6: vz, 
    bit 7: ax, bit 8: ay, bit 9:    
    
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

#按键事件功能
def key(event):
    if event.char == event.keysym: #-- standard keys
        if event.keysym == 'r':
 print("r pressed >> Set the vehicle to RTL")
            vehicle.mode = VehicleMode("RTL")
        elif event.keysym == 'l':
            print("l pressed >> Set the vehicle to LAND")
            vehicle.mode = VehicleMode("LAND")

    else: #-- non standard keys
        if event.keysym == 'Up':
            set_velocity_body(vehicle, gnd_speed, 0, 0)
        elif event.keysym == 'Down':
            set_velocity_body(vehicle,-gnd_speed, 0, 0)
        elif event.keysym == 'Left':
            set_velocity_body(vehicle, 0, -gnd_speed, 0)
        elif event.keysym == 'Right':
            set_velocity_body(vehicle, 0, gnd_speed, 0)


#主程序
#起飞，目标高度10米
arm_and_takeoff(10)

#等待键盘输入
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
print(">> Control the drone with the arrow keys. Press l for LAND mode")
root.bind_all('<Key>', key)
root.mainloop()
