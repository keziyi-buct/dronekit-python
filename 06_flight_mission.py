#使用droneKit连接无人机,下载无人机的任务并将这个任务保存在一个txt文件中，随后定义三个航点，将这三个航点作为任务上传到无人机中，并保存上传的任务为txt文件。
from dronekit import connect, VehicleMode, Command
from pymavlink import mavutil

connection_string = 'udp:127.0.0.1:14550'  # 假设使用UDP连接到无人机

# 连接到无人机
vehicle = connect(connection_string, wait_ready=True)

# 下载任务并将任务保存在txt文件中
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()

with open('mission.txt', 'w') as f:
    for cmd in cmds:
        f.write("%s\n" % cmd)

# 定义三个航点
wp1 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0,
              1, 0, 0, 0, 0, 0, 37.810664, -122.473833, 10)

wp2 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0,
              2, 0, 0, 0, 0, 0, 37.811065, -122.473853, 20)

wp3 = Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0,
              3, 0, 0, 0, 0, 0, 37.810996, -122.473478, 10)

# 将三个航点添加到任务列表中
cmds = vehicle.commands
cmds.clear()
cmds.add(wp1)
cmds.add(wp2)
cmds.add(wp3)

# 上传任务并将任务保存到txt文件中
cmds.upload()
cmds.download()
cmds.wait_ready()

with open('mission_upload.txt', 'w') as f:
    for cmd in cmds:
        f.write("%s\n" % cmd)

# 断开连接
vehicle.close()
