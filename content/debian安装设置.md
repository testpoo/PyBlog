title: debian安装设置
date: 2024-08-13
category: 系统安装
tag: debian, gnome, xfce, kde, linux

[TOC]

### 1. 下载特殊版本链接

> 2023 年 6 月 10 日： 从 Debian 12 (Bookworm) 开始，固件已包含在正常的 Debian 安装程序镜像中，用户无需再在此查找特殊版本。

- [稳定版：https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/)

- [测试版：https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/](https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/)

附驱动下载地址（可选）：

- <https://mirrors.tuna.tsinghua.edu.cn/debian-nonfree/firmware/bookworm/current/firmware.zip>

- <https://packages.debian.org/bookworm/firmware-misc-nonfree>

### 2. 制作自启动U盘

`dd if=xxx.iso of=/dev/disk`

### 3. 安装

选择非自动安装，在安装更新步骤，去掉安装更新，理由，安装更新使用的是Debian官方源，特别慢，可在安装好后，使用国内源，再安装。

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

### 6. 修改源

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

### 7. Gnome桌面设置

#### 7.1 安装软件

`sudo apt install intel-microcode fonts-noto-cjk git ibus-rime rime-data-wubi`

#### 7.2. 删除不需要软件

`apt autoremove --purge evolution libreoffice* gnome-calendar cheese gnome-chess gnome-clocks gnome-contacts evolution five-or-more four-in-a-row hitori gnome-klotski lightsoff gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles quadrapassel gnome-robots gnome-sudoku swell-foop tali gnome-taquin gnome-tetravex gnome-todo totem gnome-2048 gnome-weather goldendict rhythmbox shotwell simple-scan synaptic termit transmission-gtk yelp zhcon aisleriot iagno gnome-sound-recorder fcitx5*`

#### 7.3. 删除多余的扩展

- 删除/usr/share/gnome-shell/extensions下除user-theme以外的所有扩展

### 8. xfce桌面设置

#### 8.1. 删除软件

```
# sudo apt autoremove libreoffice* exfalso parole quodlibet synaptic --purge
sudo apt autoremove libreoffice* exfalso quodlibet synaptic xfburn --purge
sudo apt autoremove xfce4-whiskermenu-plugin xfce4-weather-plugin xfce4-wavelan-plugin xfce4-verve-plugin xfce4-timer-plugin xfce4-smartbookmark-plugin xfce4-cpufreq-plugin xfce4-cpugraph-plugin xfce4-diskperf-plugin xfce4-battery-plugin xfce4-sensors-plugin xfce4-systemload-plugin xfce4-xkb-plugin xfce4-netload-plugin xfce4-mailwatch-plugin xfce4-clipman-plugin xfce4-fsguard-plugin atril --purge
```

#### 8.2. 安装软件

`sudo apt install fcitx5 git fcitx5-rime rime-data-wubi gvfs-backends blueman yaru-theme-gtk fonts-noto-cjk webext-ublock-origin-firefox ristretto xfce4-screenshooter xfce4-taskmanager`

安装图标 `https://github.com/vinceliuice/Qogir-icon-theme`

#### 8.3. 设置

- 快捷键设置:设置-->键盘-->应用程度快捷键
- 窗口样式设置：设置-->窗口管理器-->样式+按钮布局
- 窗口管理器微调：设置-->窗口管理器微调-->辅助功能  最大化窗口时隐藏标题
- 窗口管理器微调：设置-->窗口管理器微调-->合成器  在dock窗口下显示阴影

- 主题/字体设置：外观-->样式+字体
- 设置时钟格式：%A %F %H:%M 第%V周  %F%n%H:%M  %H:%M%n%Y/%m/%d

#### 8.4 添加触摸板关启脚本

本机快捷键Fn+F8==Super+Ctrl_L

```
xfce4-mouse-settings --device="SYNA3602:00 093A:0255 Touchpad"
xfce4-mouse-settings -d "SYNA3602:00 093A:0255 Touchpad"
```

```
#!/bin/sh

dev_id=`xinput list | grep 'Touch[pP]ad' | sed -E 's/^.*id=([0-9]+).*$/\1/g'`
dev_state=`xinput --list-props $dev_id | grep 'Device Enabled' | sed -E 's/^.*:.*([01]).*$/\1/g'`

if [ $dev_state -eq 1 ]; then
    xinput disable $dev_id
    notify-send -i /home/poo/.poo/input-touchpad.png -t 1500 "触摸板已关闭"
elif [ $dev_state -eq 0 ]; then
    xinput enable $dev_id
    notify-send -i /home/poo/.poo/input-touchpad.png -t 1500 "触摸板已开启"
fi
```

#### 8.5 添加缺少的图标

xfce菜单图标替换成`/usr/share/pixmaps/xfce4_xicon4.pngl`，如果使用`yaru-theme-icon`这个图标，需要使用下面的脚本对图标进行处理。

```
#!/usr/bin/python3 env
# coding=utf-8

import os

dirs = "/usr/share/icons/Yaru/"

files = [["terminal-app.png","org.xfce.terminal.png"],
["terminal-app.png","org.xfce.terminalemulator.png"],
["filemanager-app.png","org.xfce.filemanager.png"],
["webbrowser-app.png","org.xfce.webbrowser.png"],
["edit-find.png","org.xfce.appfinder.png"],
["mail-read.png","org.xfce.mailreader.png"],
["filemanager-app.png","org.xfce.thunar.png"],
["terminal-app.png","org.xfce.terminal-settings.png"],
["terminal-app.png","org.xfce.terminal-settings.png"],
["org.gnome.TextEditor.png","org.xfce.mousepad.png"],
["system-monitor-app.png","org.xfce.taskmanager.png"],
["session-properties.png","org.xfce.session.png"],
["preferences-desktop-display.png","org.xfce.settings.display.png"],
["user-desktop.png","org.xfce.xfdesktop.png"],
["screenshot-app.png","org.xfce.screenshooter.png"],
["preferences-system-power.png","org.xfce.powermanager.png"],
["network-wired-offline-symbolic.svg","nm-device-wired.svg"],
["network-wireless-disabled-symbolic.svg","nm-no-connection.svg"],
["network-wireless-signal-none-symbolic.svg","nm-signal-00.svg"],
["network-wireless-signal-none-secure-symbolic.svg","nm-signal-00-secure.svg"],
["network-wireless-signal-weak-symbolic.svg","nm-signal-25.svg"],
["network-wireless-signal-weak-secure-symbolic.svg","nm-signal-25-secure.svg"],
["network-wireless-signal-ok-symbolic.svg","nm-signal-50.svg"],
["network-wireless-signal-ok-secure-symbolic.svg","nm-signal-50-secure.svg"],
["network-wireless-signal-good-symbolic.svg","nm-signal-75.svg"],
["network-wireless-signal-good-secure-symbolic.svg","nm-signal-75-secure.svg"],
["network-wireless-signal-excellent-symbolic.svg","nm-signal-100.svg"],
["network-wireless-signal-excellent-secure-symbolic.svg","nm-signal-100-secure.svg"],
["bluetooth.png","blueman.png"],
["bluetooth-active-symbolic.svg","blueman-tray.svg"],
["bluetooth-active-symbolic.svg","blueman-active.svg"],
["bluetooth-disconnected-symbolic.svg","blueman-disabled.svg"],
["gallery-app.png","org.xfce.ristretto.png"],
["application-x-model.png","org.xfce.settings.appearance.png"]
]

for ofile,nfile in files:
    temp =os.popen("find "+dirs+" -name "+ofile)
    lists = [x.replace(ofile,'') for x in temp.read().split('\n')]
    for li in lists:
        if li != '' and os.path.exists(li+nfile) == False:
            os.system("ln -s "+li+ofile+" "+li+nfile)
os.system("gtk-update-icon-cache /usr/share/icons/Yaru")
```

#### 8.6. 图片路径

```
/usr/share/backgrounds
```

#### 8.7. lightdm设置

```
/etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
theme-name = Yaru
icon-theme-name = Yaru
font-name = Noto Sans Mono 11
default-user-image = /usr/share/backgrounds/title.jpg
clock-format = %A %F %H:%M 第%V周
background = /usr/share/backgrounds/background.png
xft-dpi = 120
indicators = ~host;~spacer;~clock;~spacer;~a11y;~session;~power
#hide-user-image = true

/etc/lightdm/lightdm.conf
greeter-hide-users=false 前的#去掉
```

#### 8.8. 支持mtp，连接安卓

- 安装gvfs-backends


#### 8.9. 启动gtk编辑器

```
xfce4-panel -q && GTK_DEBUG=interactive xfce4-panel
重启xfce-panel:xfce4-panel -r
```

#### 8.10. 修改grub背景

```
# 使用 su - 切换到 root 下，执行 sudo update-grub
# 找到 Found backgroud image: /usr/share/images/desktop-base/desktop-grub.png
# 执行 ls -l /usr/share/images/desktop-base/desktop-grub.png
# 找到 /etc/alternatives/desktop-grub
# 执行 ls -l /etc/alternatives/desktop-grub
# 找到 /usr/share/desktop-base/active-theme/grub/grub-4x3.png 替换
# 注：必须是png格式
```

#### 8.11. 添加右键

```
ln -s %f 'Link to %n'
Create a Link
创建链接
Create a symbolic link for each selected item
给每个选择的项目创建一个链接

pkexec thunar %F
Open as Root
管理员打开
Open the folder with administration
管理员打开文件夹

catfish %f
Search
搜索
Search for Files
搜索文件
```

#### 8.12. thunar侧边栏添加位置

- 点击文件右键`send to-->Side Panel`

#### 8.13. 启动花屏

```
xfwm4-->vblank_mode=off
```

#### 8.14. 添加gtk.css

- 路径`~/config/gtk3.0/gtk.css`

```
#pulseaudio-button image,#xfce4-power-manager-plugin image,#xfce4-notification-plugin image{
            -gtk-icon-transform: scale(0.4);
}

#clock-button {font-size: 14px;}

#indicator-button* { -gtk-icon-transform: scale(1.2); }

#whiskermenu-window {
   background-color: #ffbba4;
   background-image: linear-gradient(#e66465, #9198e5);
   color: #ffffff; }

calendar.highlight { color: #e95420; }
calendar {padding: 0 5px; font-weight: bold;border-radius: 5px;font-size: 14px;border: none;}
```

### 9. kde桌面设置

#### 9.1. 安装软件

`sudo apt install fonts-noto-cjk git fcitx5-rime rime-data-wubi plasma-calendar-addons`

#### 9.2. 删除不需要软件

`apt autoremove --purge kmail kaddressbook korganizer okular knotes akregator konqueror kwalletmanager k3b juk dragonplayer gimp imagemagick* kontrast kmenuedit qt5-style-kvantum kdeconnect* kmouth kmousetool kmag xterm`

#### 9.3. 安装图标主题

- 通过`https://github.com/yeyushengfan258/Win11-icon-theme`下载

- 进入`Win11-icon-theme`目录，执行`./install.sh -a`命令

#### 9.4. 安装窗口装饰

- 通过`https://github.com/vinceliuice/Colloid-kde/`下载

- 安装窗口装饰元素`Colloid-light-round`到`~/.local/share/aurorae/themes/`下

#### 9.5. 安装SDDM主题

- 通过`https://github.com/MarianArlt/kde-plasma-chili`下载

- 进入`kde-plasma-chili`目录，执行`cp -r kde-plasma-chili /usr/share/sddm/themes`命令

#### 9.6. 解决无法更换头像

- 这是账号服务的一个缺陷: 打开`sudo nano /usr/lib/systemd/system/accounts-daemon.service`文件，修改`PrivateTmp=true`为`PrivateTmp=false`，然后重启即可解决问题。

#### 9.7. 修改设置

- 桌面背景修改：设置-->更改壁纸-->壁纸类型：每日一图-->提供：必应

- 双击打开文件：设置-->点击文件或文件夹时-->选中他们

- 去掉程序特效：设置-->外观-->光标-->配置程序启动动效，沟选“无动效”，沟去“启动动效”。

- 去掉欢迎屏幕：设置-->外观-->欢迎屏幕选无。

- 锁屏背景修改：设置-->工作区行为-->锁屏-->配置-->壁纸类型：每日一图-->提供：必应

- 修改登录画面：设置-->开机与关机-->登录屏幕(SDDM)-->选择安装的新画面

- 修改用户头像：设置-->用户-->修改用户头像

- 触摸板设置：设置-->输入设备-->触摸板-->手指轻触

- 绽放设置：设置-->显示器配置-->全局缩放率：125% 

### 10. rime输入法设置

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

- fcitx5-rime

```
sudo apt install fcitx-rime rime-data-wubi
nano ~/.local/share/fcitx5/rime/default.custom.yaml
patch:
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
```
