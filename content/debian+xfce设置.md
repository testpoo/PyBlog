title: debian+xfce设置
date: 2021-05-10
category: debian
tag: xfce

[TOC]

### 1. 安装软件

`sudo apt install fonts-wqy-zenhei git fcitx5-rime rime-data-wubi gvfs-backends blueman xinput yaru-theme-gtk yaru-theme-icon`

### 2. 删除软件

```
# sudo apt autoremove libreoffice* exfalso parole quodlibet synaptic --purge
sudo apt autoremove libreoffice* exfalso quodlibet synaptic --purge
```

### 3. 设置

- 快捷键设置:设置-->键盘-->应用程度快捷键
- 窗口样式设置：设置-->窗口管理器-->样式+按钮布局
- 窗口管理器微调：设置-->窗口管理器微调-->辅助功能  最大化窗口时隐藏标题
- 窗口管理器微调：设置-->窗口管理器微调-->合成器  在dock窗口下显示阴影
- 主题/字体设置：外观-->样式+字体
- 设置时钟格式：%A %F %H:%M 第%V周  %F%n%H:%M  %H:%M%n%Y/%m/%d

#### 3.1 添加触摸板关启脚本

本机快捷键Fn+F8==Super+Ctrl_L
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

#### 3.2 添加缺少的图标

xfce菜单图标替换成`/usr/share/pixmaps/xfce4_xicon4.pngl`

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

### 4. 图片路径

```
/usr/share/backgrounds
```

### 5. lightdm设置

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

### 6. 支持mtp，连接安卓

- 安装gvfs-backends


### 7. 启动gtk编辑器

```
xfce4-panel -q && GTK_DEBUG=interactive xfce4-panel
重启xfce-panel:xfce4-panel -r
```

### 8. 修改grub背景

```
# 使用 su - 切换到 root 下，执行 sudo update-grub
# 找到 Found backgroud image: /usr/share/images/desktop-base/desktop-grub.png
# 执行 ls -l /usr/share/images/desktop-base/desktop-grub.png
# 找到 /etc/alternatives/desktop-grub
# 执行 ls -l /etc/alternatives/desktop-grub
# 找到 /usr/share/desktop-base/active-theme/grub/grub-4x3.png 替换
# 注：必须是png格式
```

### 9. 添加右键

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

### 10. thunar侧边栏添加位置

- 点击文件右键`send to-->Side Panel`

### 11. 启动花屏

```
xfwm4-->vblank_mode=off
```

### 12. 添加gtk.css

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

### 13. 安装xfce4-docklike-plugin

- 安装xfce4-docklike-plugin合并启动器和窗口管理器

```
# 编译使用到的软件
apt install xfce4-dev-tools libglib2.0-dev libx11-dev build-essential libgtk-3-dev pkg-config devhelp libwnck-3-dev libxfce4ui-2-dev libxfce4panel-2.0-dev
```

- 编译

```
./autogen.sh --prefix=/home/poo/usr
make
sudo make install
# 把usr复制到根目录下，目前有不显示中文的问题，原因还没有找到
```