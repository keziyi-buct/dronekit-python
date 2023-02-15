dronekit 是在python中常用的一种开发的库，这个库是可以直接用来控制无人机。
首先需要配置环境，安装几个库：dronekit,silt,pymavlink,mavproxy.
'''
pip install dronekit 
pip install dronekit-sitl
sudo -H pip install pymavlink==2.4.8
sudo -H pip install mavproxy==1.7.1
'''
后面两个我之所以和前两个正常的PIP不同，这里是因为我刷了大量的论坛和博客，这里这么安装的话不会报错，也可以尝试一下正常安装
安装完成后开两个终端，分别运行仿真软件和通讯端口仿真，两个终端分别输入：
'''
dronekit-sitl  copter --home=31.9386595,118.7898506,3,30 --model=quad
mavproxy.py --master=tcp:127.0.0.1:5760 --out=127.0.0.1:14550 
'''
out后面的这个是提供给dronekit 连接的UDP|TCP的

