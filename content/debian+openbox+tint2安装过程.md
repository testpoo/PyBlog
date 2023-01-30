title: debian+openbox+tint2安装过程
date: 2022-07-18
category: debian
tag: openbox,tint2

[TOC]

### 1. 安装软件

`apt install openbox xinit tint2 sakura pcmanfm ristretto fcitx-rime librime-data-wubi lxappearance xarchiver pulseaudio blueman sudo git intel-microcode fonts-noto-cjk slock light`

```
light 亮度
slock 锁屏
neofetch 系统信息
tint2 任务栏
sakura 设置背景
lxappearance 外观
pulseaudio 声音驱动
blueman 蓝牙

# 可选
jgmenu 菜单：进程杀不死
libnotify-bin 通知
dunst 通知
volumeicon-alsa 音量控制
network-manager-gnome 网络
mate-power-manager 电源
```

### 2. 设置

- openbox

**复制配置文件**

```
$ mkdir -p ~/.config/openbox
# openbox有以下文件{rc.xml,menu.xml,autostart,environment}
$ cp /etc/xdg/openbox/* ~/.config/openbox/
```

**设置启动项**

```
# autostart.sh

tint2 &
pcmanfm --desktop &
blueman-applet &
#volumeicon &
```

```

**添加快捷键**

```
# keyboard中加入如下代码 声音和亮度快捷键绑定

    <!--自定义-->
    <keybind key="XF86AudioMute">
      <action name="Execute">
        <execute>pactl set-sink-mute @DEFAULT_SINK@ toggle</execute>
      </action>
    </keybind>
    <keybind key="XF86AudioLowerVolume">
      <action name="Execute">
        <execute>pactl set-sink-volume @DEFAULT_SINK@ -5%</execute>
      </action>
    </keybind>
    <keybind key="XF86AudioRaiseVolume">
      <action name="Execute">
        <execute>pactl set-sink-volume @DEFAULT_SINK@ +5%</execute>
      </action>
    </keybind>
    <keybind key="XF86MonBrightnessUp">
      <action name="Execute">
        <execute>light -A 5</execute>
      </action>
    </keybind>
    <keybind key="XF86MonBrightnessDown">
      <action name="Execute">
        <execute>light -U 5</execute>
      </action>
    </keybind>
```

- tint2

```
# 亮度
echo "☀️$(light|cut --delimiter=. -f1)%"
```

```
#!/bin/bash
# 增加亮度
light -A 5
notify-send "当前亮度为: $(light|cut --delimiter=. -f1)%"
```

```
#!/bin/bash
# 减少亮度
light -U 5
notify-send "当前亮度为: $(light|cut --delimiter=. -f1)%"
```

```
# 声音(volume.py)

# coding=utf-8

import os

mute = os.popen('pactl get-sink-mute @DEFAULT_SINK@').read()
volume = os.popen('pactl get-sink-volume @DEFAULT_SINK@').read()
if mute[6] == "否":
    print('🔊'+volume[29:32])
else:
    print('🔇'+volume[29:32])
```

```
# 网络(network.py)

# coding=utf-8

import os

network = os.popen('hostname -I').read()

if network == '\n':
    print('🌐Down')
else:
    print('📶Nokia')
```