## 准备

**为系统添加swap空间（基于debian 10）**

**检查系统的交换信息**

\# 显示swap状态

`sudo swapon --show`

\# 显示系统可用内存

`free -h`

**检查磁盘上的可用空间**

`df -h`

**创造交换文件**

\# 返回根目录

`cd ~`

\# 创建大小为4G的空间

`sudo fallocate -l 4G /SwapFile`

\# 显示准备用作swap的空间大小

`ls -lh /SwapFile`

建议把swap开到4G

启用交换文件

\# 给权限

`sudo chmod 600 /SwapFile`

\# 创建swap文件

`sudo mkswap /SwapFile`

\# 打开swap

`sudo swapon /SwapFile`

\# 检查swap，同第一步

`sudo swapon --show`

`free -h`

如果之后想要关闭交换文件，输入cd ~ && sudo swapoff /SwapFile

**令交换文件永久化**

\# 备份原文件

`sudo cp /etc/fstab /etc/fstab.bak`

\# 添加交换文件的信息

`echo '/SwapFile none swap sw 0 0' | sudo tee -a /etc/fstab`



## 安装依赖

\# 先检查下升级

`sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade`

\# 核心依赖

`sudo apt-get install git cmake libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev`

\# 图形相关依赖，realsense-viewer需要用到

`sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev`



## 编译

**下载 \*Realsense SDK\***

`cd ~`

`git clone https://github.com/IntelRealSense/librealsense.git`

**编译准备**

`cd librealsense`

`mkdir build && cd build`

`cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_EXAMPLES=true -DFORCE_RSUSB_BACKEND=ON -DBUILD_PYTHON_BINDINGS:bool=true -DPYTHON_EXECUTABLE=/usr/bin/python3.9`

**-DFORCE_RSUSB_BACKEND=ON 必选，强制LIBUVC后端，否则你要自己给内核打补丁。**

**-DPYTHON_EXECUTABLE=/usr/bin/python3.9 看你自己python的版本，进/usr/bin看一下就知道了**

有关更多的编译选项，请参照官方的[这篇wiki](https://dev.intelrealsense.com/docs/build-configuration)

**编译**

`sudo make uninstall && sudo make clean && make -j4`

`make -j后的数字为编译时用到的核心数，不知道自己系统核心数的可以通过命令nproc查询，有内存跟不上的请自行降低编译核心数`

**安装先前编译内容**

`sudo make install`



## 将安装内容添加到环境变量

`sudo nano ~/.bashrc`

\# 在文件尾部输入

`export LD_LIBRARY_PATH=/usr/local/lib/aarch64-linux-gnu:$LD_LIBRARY_PATH`

`export PYTHONPATH=/usr/local/lib/aarch64-linux-gnu:/usr/lib/python3/dist-packages/pyrealsense2:$PYTHONPATH`

\# 保存并退出编辑器

`source ~/.bashrc`

这个环境变量的具体设置和你的安装环境有关，我的不一定和你一样，但你可以留意你make install之后系统显示的文件保存路径，一个是.so动态库文件保存到了/xxx/xxx/lib，一个是python的包装到了/xxx/xxx/pyrealsense2，你要填到环境变量里的就是这两个路径



## 设置udev规则

\# 进入librealsense目录下

`sudo ./scripts/setup_udev_rules.sh`



## 基础测试

\# 进入python3

`python3`

`\>>> import pyrealsense2 as rs`

`\>>> dir(rs)`