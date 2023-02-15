#记住运行代码前一定要先配置虚拟的仿真或者连接无人机，并且搭建环境，要不就报错
# 上述代码首先通过connect函数连接无人机，wait_ready=True表示在等待无人机状态准备就绪时阻塞程序。之后，使用无人机对象的属性打印无人机状态信息，例如：

# vehicle.version打印无人机固件版本信息；
# vehicle.location.global_frame打印无人机全球定位信息；
# vehicle.battery打印无人机电池信息；
# vehicle.mode打印无人机模式信息。
# 最后，使用vehicle.close()关闭链接。

from dronekit import connect, VehicleMode

# 连接无人机
connection_string = '/dev/ttyUSB0' # 或者是 'udp:127.0.0.1:14550'
vehicle = connect(connection_string, wait_ready=True)

# 打印无人机状态信息
print("Autopilot Firmware version: %s" % vehicle.version)
print("Global Location: %s" % vehicle.location.global_frame)
print("Battery: %s" % vehicle.battery)
print("Mode: %s" % vehicle.mode)

# 关闭链接
vehicle.close()
