title: debian+openbox+tint2安装过程
date: 2022-07-18
category: debian
tag: openbox,tint2

[TOC]

### 1. 下载链接

<https://www.debian.org/download>

### 2. 下载驱动

<https://mirrors.tuna.tsinghua.edu.cn/debian-nonfree/firmware/bookworm/current/firmware.zip>

### 3. 制作自启动U盘

### 4. 安装

### 5. 去掉debain开机启动项停留的5秒和电池的问题

```
su root
nano /etc/sudoers添加 poo ALL=(ALL:ALL) ALL
nano /etc/default/grub
找到 GRUB_DEFAULT=x,并将x改为希望启动系统的序号,默认 x == 0，即默认启动项是 Debian,启动项从上往下数分别是 0 、 1 、 2 。。。
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

### 6. 修改源

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bookworm-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security bookworm-security main contrib non-free
```

### 7. 安装软件

`apt install openbox xinit tint2 jgmenu sakura thunar feh fcitx-rime librime-data-wubi lxappearance xarchiver pulseaudio blueman thunar-archive-plugin neofetch ristretto intel-microcode fonts-noto-cjk slock light`

```
light-亮度
slock-锁屏
jgmenu-菜单
neofetch-系统信息
tint2-任务栏
sakura-设置背景
lxappearance-外观
pulseaudio-声音驱动
blueman-蓝牙
```

### 8. 设置

- openbox

```
# autostart.sh

tint2 &
fcitx &
blueman-applet &
feh --bg-scale "/home/poo/.poo/bg.jpg" &
```
```
# keyboard中加入如下代码

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

- jgmenu

```
# jgmenurc

stay_alive           = 1
tint2_look           = 0
position_mode        = fixed
terminal_exec        = termite
terminal_args        = -e
menu_width           = 200
menu_padding_top     = 40
menu_padding_right   = 2
menu_padding_bottom  = 5
menu_padding_left    = 2
menu_radius          = 0
menu_border          = 1
menu_halign          = left
sub_hover_action     = 1
item_margin_y        = 5
item_height          = 30
item_padding_x       = 8
item_radius          = 0
item_border          = 0
sep_height           = 5
font                 = Ubuntu 15px
icon_size            = 30
color_menu_bg        = #eeeeee 100
color_norm_bg        = #2b303b 0
color_norm_fg        = #000000 100
color_sel_bg         = #8fa1b3 60
color_sel_fg         = #2b303b 100
color_sep_fg         = #8fa1b3 40
```
```
# append.csv

^sep()
退出,^checkout(exit),system-shutdown
^tag(exit)
锁屏,slock,system-lock-screen
退出,openbox --exit,system-log-out
挂起,systemctl -i suspend,system-log-out
休眠,systemctl -i hibernate,system-hibernate
重启,systemctl -i reboot,system-reboot
关机,systemctl -i poweroff,system-shutdown
```
```
# prepend.csv

@rect,,5,10,190,30,2,left,top,#000000 0,#656565 50,
@search,,10,10,185,30,2,left,top,#eeeeee 80,#000000 0,
^sep()
终端,x-terminal-emulator,utilities-terminal
文件,thunar,system-file-manager
火狐,firefox-esr,firefox
^sep()
```

- tint2

```
# 亮度
echo "☀️$(light|cut --delimiter=. -f1)%"

# 声音(volume.py)

# coding=utf-8

import os

mute = os.popen('pactl get-sink-mute @DEFAULT_SINK@').read()
volume = os.popen('pactl get-sink-volume @DEFAULT_SINK@').read()
if mute[6] == "否":
	print('🔊'+volume[29:32])
else:
	print('🔇'+volume[29:32])
  
# 网络(network.py)

# coding=utf-8

import os

network = os.popen('hostname -I').read()

if network == '\n':
	print('📶Down')
else:
	print('📶Nokia')
```

### 9. 安装第三方软件

```
wps:https://linux.wps.cn/
baidu网盘:https://pan.baidu.com/download 需要依赖:https://blog.csdn.net/weixin_45447477/article/details/115188938
vscode:https://code.visualstudio.com/
QQ音乐：https://y.qq.com/download/download.html
QQ：https://im.qq.com/linuxqq/download.html
sublime: https://www.sublimetext.com/download
typora: https://www.typora.io/#linux
Motrix: https://motrix.app/
```

### 10. 缺少驱动

```
# 添加驱动
https://packages.debian.org/bookworm/firmware-misc-nonfree
```

### 11. 安装输入法

```
# sudo apt install ibus-rime librime-data-wubi
# /home/poo/.config/ibus/rime/default.custom.yaml
sudo apt install fcitx-rime librime-data-wubi
/home/poo/.config/fcitx/rime/default.custom.yaml
patch:
  "style/horizontal": true
  "menu/page_size": 5

  schema_list:
    - schema: wubi_pinyin
    - schema: luna_pinyin_simp
    - schema: wubi86
```
