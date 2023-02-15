from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

# 连接到无人机
connection_string = 'udp:127.0.0.1:14551'  # 连接字符串
vehicle = connect(connection_string, wait_ready=True)  # 连接到无人机

# 控制飞机起飞
target_altitude = 10  # 目标高度为10米

# 控制飞机起飞
print("起飞中...")
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
while not vehicle.armed:
    time.sleep(1)

# 控制飞机飞行到目标高度
print("飞行中...")
vehicle.simple_takeoff(target_altitude)
while True:
    current_altitude = vehicle.location.global_relative_frame.alt
    if current_altitude >= target_altitude * 0.95:
        print("已达到目标高度")
        break
    time.sleep(1)

# 启动返航模式
print("返回中...")
vehicle.mode = VehicleMode("RTL")

# 等待飞机降落
while True:
    if not vehicle.armed:
        print("降落成功")
        break
    time.sleep(1)

# 断开连接
vehicle.close()




# dronekit.VehicleMode 是 dronekit 中用于表示无人机飞行模式的类，其包含的属性和方法可以用于设置或获取无人机的模式。根据 dronekit 的文档，VehicleMode 中定义了如下 12 种无人机模式：
# VehicleMode("STABILIZE"): 基本稳定模式，无人机不会自动平衡，但可以通过遥控器进行控制。
# VehicleMode("ACRO"): 亲身操纵模式，无人机完全由遥控器控制。
# VehicleMode("ALT_HOLD"): 定高模式，无人机会自动控制高度。
# VehicleMode("AUTO"): 自动模式，无人机会按照预设好的航点进行飞行。
# VehicleMode("GUIDED"): 引导模式，无人机跟随遥控器进行控制，但也可以设置目标点进行引导。
# VehicleMode("LOITER"): 待机模式，无人机会自动悬停在当前位置。
# VehicleMode("RTL"): 返航模式，无人机会自动返航到起飞点。
# VehicleMode("CIRCLE"): 圆航模式，无人机会围绕某个点进行圆周飞行。
# VehicleMode("LAND"): 降落模式，无人机会自动降落到地面。
# VehicleMode("DRIFT"): 飘移模式，无人机会在风力作用下进行漂移。
# VehicleMode("SPORT"): 运动模式，无人机响应操作更快、更灵敏，适合运动飞行。
# VehicleMode("FLIP"): 翻转模式，无人机会进行翻转动作。
# 需要注意的是，不同型号的无人机可能支持的模式会有所不同。同时，VehicleMode 也支持自定义无人机模式，用户可以根据自己的需求来定义新的模式。
# 这里经常使用的是起飞时用引导模式，建返航用RTL，然后降落用LAND。