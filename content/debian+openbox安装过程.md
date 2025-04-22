title: debian+openbox安装过程
date: 2022-07-18
category: 系统安装
tag: debian, openbox, tint2, linux

[TOC]

### 1. 连接wifi

- 查看网卡：`ip a`

- 先安装 `wpa_supplicant`

- 配置网络参数：`su -l -c "wpa_passphrase WIFI名字 WIFI密码 > /etc/wpa_supplicant/wpa_supplicant.conf"`

- 配置接口
  
  - 查看WIFI网卡名称
  - 编辑文件/etc/network/interfaces

- 添加接口参数如下：

```
auto wlp1s0 #(wlp1s0 为网卡名)
iface wlp1s0 inet dhcp
    wpa-deriver wext
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

- 启动网卡：`ifup wlp1s0` 需要在`root`或`su - `下重启

### 2. 修改源

<https://mirrors.tuna.tsinghua.edu.cn/help/debian/>

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-free non-free-firmware
# deb https://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
# # deb-src https://security.debian.org/debian-security bookworm-security main contrib non-free non-free-firmware
```

### 3. 安装软件

`apt install openbox xinit tint2 sakura pcmanfm ristretto fcitx-rime rime-data-wubi lxappearance xarchiver pulseaudio blueman sudo git intel-microcode fonts-noto-cjk slock light jgmenu chromium chromium-l10n webext-ublock-origin-chromium`

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

### 4. 将当前用户加入sudo

```
# 方法一
su root
nano /etc/sudoers添加 username ALL=(ALL:ALL) ALL

# 方法二
useradd -a -G sudo username
reboot
```

### 5. 去掉debain开机启动项停留的5秒和电池的问题

```
nano /etc/default/grub
找到 GRUB_DEFAULT=x,并将x改为希望启动系统的序号,默认 x == 0，即默认启动项是 Debian,启动项从上往下数分别是 0 、 1 、 2 。。。
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

### 6. 安装输入法

- fcitx-rime

```
sudo apt install fcitx-rime rime-data-wubi
nano ~/.config/fcitx/rime/default.custom.yaml
patch:
  "style/horizontal": true
  "menu/page_size": 5

  schema_list:
    - schema: wubi_pinyin
    - schema: luna_pinyin_simp
    - schema: wubi86
```

- ibus-rime

```
sudo apt install ibus-rime rime-data-wubi
nano ~/.config/ibus/rime/default.custom.yaml
patch:
  schema_list:
    - schema: wubi_pinyin
    - schema: luna_pinyin_simp
    - schema: wubi86

nano ~/.config/ibus/rime/build/ibus_rime.yaml

# 修改ibus_rime.yaml中horizontal为true

style:
   horizontal: true

# 重新部署 ibus-rime
```

### 7. 触摸板修改

```
sudo nano /usr/share/X11/xorg.conf.d/40-libinput.conf

Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"

        Option "Tapping" "on" # 触摸以点击
        Option "ClickMethod" "clickfinger" # 触摸板不再拥有中右键区域的区分，与之代替的是双指代表右键，三指代表中键。
        Option "NaturalScrolling" "true" # 自然滚动（反方向滚动）
#        Option "ScrollMethod" "edge" # 边缘滚动页面
EndSection
```

### 8. 设置dpi

```
nano .Xresources

Xft.dpi:120
sudo xrdb ~/.Xresources
reboot
```

### 9. 启动OpenBox

编辑（不存在即新建）文件~/.bash_profile（在tty下登录是不会执行.bashrc的），新增一行内容如下：

```
if [ -z $DISPLAY ] && [ $(tty) = "/dev/tty1" ];then
    startx
fi
# 查看Ctrl-Alt-F1对应的那个tty
echo $(tty)
```

### 10. 设置

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

### 11. 详细配置文件

`https://github.com/testpoo/obconfig`
