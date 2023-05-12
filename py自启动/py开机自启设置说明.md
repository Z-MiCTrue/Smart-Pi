1. 编写unit文件，文件名要以.service结尾，这里我保存为/home/pi/auto_process.py

内容:

```
[Unit]
Description=My service
After=network.target

[Service]
Restart=on-failure
RestartSec=30
ExecStart=/usr/bin/python3 -u /home/pi/Documents/auto_process.py
User=pi

[Install] 
WantedBy=multi-user.target
```

其中，auto_process.py 是一个多进程启动管理脚本，修改 *func_list.txt* 内的命令即可设置启动的进程，*func_list.txt* 中是一个列表，列表长度即为开启进程数。本质上这是一个开启多个进程通过命令中断执行多程序的脚本。



2. 将该文件mystart.service复制到/etc/systemd/system目录下

```
sudo cp /home/pi/auto-service.service /etc/systemd/system/auto-service.service
```

 

3. 使用systemctl管理服务

·启动服务

```
sudo systemctl start auto-service.service
```

·查看服务状态

```
systemctl status auto-service.service
```

·使用journalctl查看该服务的输出

```
journalctl -u auto-service -e
```

·停止服务

```
sudo systemctl stop auto-service.service
```

4. 设置开机自启动

·开启

```
sudo systemctl enable auto-service.service
```

·关闭

```
sudo systemctl disable auto-service.service
```

·添加或修改配置文件后，需要重新加载

```
sudo systemctl daemon-reload
```

·查看输出与状态

```
journalctl -u mystart -e
```

 
