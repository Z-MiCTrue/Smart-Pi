## 安装依赖

\# 先检查下升级

`sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade`

\# 核心依赖

`sudo apt-get install -y git cmake libusb-1.0-0-dev`

\# 切换到目录

`cd openvino`

\# python依赖

`python3 -m pip install --upgrade pip`

`python3 -m pip install -r src/bindings/python/src/compatibility/openvino/requirements-dev.txt`

\# 安装编译依赖文件

`chmod +x install_build_dependencies.sh`

`./install_build_dependencies.sh`

\# 清除缓存

`hash -r`

\# 创造编译文件夹

`mkdir build && cd build`

\# 选择编译选项

`cmake -DCMAKE_BUILD_TYPE=Release -DENABLE_MKL_DNN=OFF -DENABLE_CLDNN=ON -DENABLE_PYTHON=ON -DENABLE_GNA=OFF -DENABLE_SSE42=OFF -DTHREADING=SEQ -DENABLE_SAMPLES=OFF -DPYTHON_EXECUTABLE=/usr/bin/python3.9 -DPYTHON_INCLUDE_DIR=/usr/include/python3.9 -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.9.so ..`

 

##  编译

`make -j4`

 

## 安装先前编译内容

`sudo make install`



## 将安装内容添加到环境变量

`cd ~/Software/openvino/scripts/setupvars`

`mkdir python`

`cp -rf  ~/Software/openvino/bin/aarch64/Release/lib/python_api/python3.9 ./python`

\# 运行脚本

`source ~/Software/openvino/scripts/setupvars/setupvars.sh`

\# 编辑bash配置文件

`vim ~/.bashrc`

\# 在文件尾部输入以下内容

`source ~/Software/openvino/scripts/setupvars/setupvars.sh`

\# 退出并保存文件，更新环境变量

`source ~/.bashrc`

 

 

## NCS2 设备的额外安装步骤

将目前的Linux用户添加到用户组，在此步骤执行完成后，您将需要重新登录系统

`sudo usermod -a -G users "$(whoami)"`

安装usb规则

\# 规则内部内容

`cat <<EOF > 97-myriad-usbboot.rules`

`SUBSYSTEM=="usb", ATTRS{idProduct}=="2485", ATTRS{idVendor}=="03e7", GROUP="users", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1"`

`SUBSYSTEM=="usb", ATTRS{idProduct}=="f63b", ATTRS{idVendor}=="03e7", GROUP="users", MODE="0666", ENV{ID_MM_DEVICE_IGNORE}="1"`

`EOF`

\# 把创建的规则复制到系统内部

`sudo cp 97-myriad-usbboot.rules /etc/udev/rules.d/`

\# 重载规则

`sudo udevadm control --reload-rules`

\# 设置trigger

`sudo udevadm trigger`

\# 创建动态链接

`sudo ldconfig`

\# 删除刚刚创建在本地的usb规则

`rm 97-myriad-usbboot.rules`



## 基础测试

\# 进入python3

`python3`

`>>> from openvino.inference_engine import IECore`

`>>> dir(IECore)`

 