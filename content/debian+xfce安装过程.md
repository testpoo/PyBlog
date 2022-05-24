title: debian+xfce安装过程
date: 2021-05-10
category: debian
tag: xfce

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

`# sudo apt install filezilla stacer meld uget aria2 intel-microcode fonts-noto-cjk arc-theme moka-icon-theme`

`sudo apt install filezilla stacer meld intel-microcode fonts-noto-cjk arc-theme git fcitx-rime librime-data-wubi gvfs-backends papirus-icon-theme blueman catfish drawing`

### 8. 删除软件

```
# sudo apt autoremove libreoffice* exfalso parole quodlibet synaptic --purge
sudo apt autoremove libreoffice* exfalso quodlibet synaptic --purge
```

### 9. 设置

- 快捷键设置:设置-->键盘-->应用程度快捷键
- 窗口样式设置：设置-->窗口管理器-->样式+按钮布局
- 窗口管理器微调：设置-->窗口管理器微调-->辅助功能  最大化窗口时隐藏标题
- 主题/字体设置：外观-->样式+字体
- 设置时钟格式：%A %F %H:%M 第%V周  %F%n%H:%M

### 10. 安装第三方软件

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

### 11. 缺少驱动

```
# 添加驱动
https://packages.debian.org/bookworm/firmware-misc-nonfree
```

### 12. 图片路径

```
/usr/share/backgrounds
```

### 13. lightdm设置

```
/etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
theme-name = Arc
icon-theme-name = Moka
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

### 14. 安装输入法

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

### 15. 支持mtp，连接安卓

- 安装gvfs-backends

### 16. 设置关闭按钮

```
安装xdotool
[Desktop Entry]
Name=close
GenericName=window close
Comment=window close
Exec=sh -c "xdotool key alt+F4"
Terminal=false
Icon=window-close-symbolic

[Desktop Entry]
Name=minimize
GenericName=window minimize
Comment=window minimize
Exec=sh -c "xdotool key alt+F9"
Terminal=false
Icon=window-minimize-symbolic

[Desktop Entry]
Name=maximize
GenericName=window maximize
Comment=window maximize
Exec=sh -c "xdotool key alt+F10"
Terminal=false
Icon=window-maximize-symbolic

当下的激活窗口，使用包 xdotool：
xdotool getwindowfocus windowkill
```

### 17. 启动gtk编辑器

```
xfce4-panel -q && GTK_DEBUG=interactive xfce4-panel
重启xfce-panel:xfce4-panel -r
```

### 18. 修改grub背景

```
/usr/share/desktop-base/homeworld-theme/grub/grub_background.sh
WALLPAPER=/usr/share/backgrounds/background.png
注：必须是png格式
```

### 19. 添加右键

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

### 20. thunar侧边栏添加位置

- 点击文件右键`send to-->Side Panel`

### 21. 启动花屏

```
xfwm4-->vblank_mode=off
```

### 22. 添加gtk.css

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

calendar.highlight { color: red; }
calendar {padding: 0 10px; font-weight: bold;}
```

### 23. 安装xfce4-docklike-plugin

- 安装xfce4-docklike-plugin合并启动器和窗口管理器

```
# 编译使用到的软件
apt install xfce4-dev-tools
apt install libglib2.0-dev
apt install libx11-dev
apt install build-essential libgtk-3-dev pkg-config devhelp
apt install libwnck-3-dev
apt install libxfce4ui-2-dev
apt install libxfce4panel-2-dev
apt install libxfce4panel-2.0-dev
```

- 汉化内容如下(zh_CN.po)：

放到`xfce4-docklike-plugin\po`目录中编译

```
# SOME DESCRIPTIVE TITLE.
# Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
# This file is distributed under the same license as the PACKAGE package.
# FIRST AUTHOR <pu_yawei@qq.com>, YEAR 2022.
#
msgid ""
msgstr ""
"Project-Id-Version: \n"
"Report-Msgid-Bugs-To: \n"
"POT-Creation-Date: 2022-03-31 19:31-0700\n"
"PO-Revision-Date: 2022-03-31 19:31+0800\n"
"Language-Team: \n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"
"Content-Transfer-Encoding: 8bit\n"
"X-Generator: Poedit 2.2.2\n"
"Plural-Forms: nplurals=1; plural=0;\n"
"Last-Translator: \n"
"Language: zh_CN\n"

#: ../src/Wnck.cpp:198
msgid "Pinned to Dock"
msgstr "固定到任务栏"

#: ../src/Wnck.cpp:198
msgid "Pin to Dock"
msgstr "固定到任务栏"

#: ../src/Wnck.cpp:199
msgid "Edit Launcher"
msgstr "编辑启动器"

#: ../src/Wnck.cpp:226
msgid "Close All"
msgstr "关闭全部"

#: ../src/Wnck.cpp:245
msgid "Remove"
msgstr "移除"

#: ../src/SettingsDialog.cpp:197
#, c-format
msgid "<b>Only the first %u hotkeys(s) are enabled.</b>\n"
msgstr "<b>仅启用第一个 %u 热键。</b>\n"

#: ../src/SettingsDialog.cpp:199
#, c-format
msgid ""
"The &lt;SUPER&gt;+%u combination seems already in use by another process.\n"
"Check your Xfce settings."
msgstr ""
"&lt;SUPER&gt;+%u组合似乎已被占用，\n"
"检查您的 Xfce 设置。"

#. namespace SettingsDialog
#: ../src/docklike.desktop.in.h:1
msgid "A modern, minimalist taskbar for Xfce"
msgstr "适用于 Xfce 的现代简约任务栏"

#: ../src/_dialogs.xml.h:1
msgid "_Help"
msgstr "_帮助"

#: ../src/_dialogs.xml.h:2
msgid "_Close"
msgstr "_关闭"

#: ../src/_dialogs.xml.h:3
msgid "Don't show the window list for a single window"
msgstr "不显示单个窗口的窗口列表"

#: ../src/_dialogs.xml.h:4
msgid "Only show applications on the current workspace"
msgstr "仅显示当前工作区上的应用程序"

#: ../src/_dialogs.xml.h:5
msgid "Only show applications on the current display"
msgstr "仅在当前显示屏上显示应用程序"

#: ../src/_dialogs.xml.h:6
msgid "Show preview thumbnails for open windows"
msgstr "显示打开窗口的预览缩略图"

#: ../src/_dialogs.xml.h:7
msgid "Show the number of open windows (if more than 2)"
msgstr "显示打开的窗口数（如果超过 2 个）"

#: ../src/_dialogs.xml.h:8
msgid "Behavior"
msgstr "行为"

#: ../src/_dialogs.xml.h:9
msgid "Indicator style:"
msgstr "指标样式："

#: ../src/_dialogs.xml.h:10
msgid "Bars"
msgstr "条"

#: ../src/_dialogs.xml.h:11
msgid "Dots"
msgstr "点"

#: ../src/_dialogs.xml.h:12
msgid "Ciliora"
msgstr "细条"

#: ../src/_dialogs.xml.h:13
msgid "Circles"
msgstr "圆形"

#: ../src/_dialogs.xml.h:14
msgid "Rectangles"
msgstr "矩形"

#: ../src/_dialogs.xml.h:15
msgid "None"
msgstr "无"

#: ../src/_dialogs.xml.h:16
msgid "Indicator orientation:"
msgstr "指标方向："

#: ../src/_dialogs.xml.h:17
msgid "Automatic"
msgstr "自动"

#: ../src/_dialogs.xml.h:18
msgid "Bottom"
msgstr "底部"

#: ../src/_dialogs.xml.h:19
msgid "Right"
msgstr "右边"

#: ../src/_dialogs.xml.h:20
msgid "Top"
msgstr "顶部"

#: ../src/_dialogs.xml.h:21
msgid "Left"
msgstr "左边"

#: ../src/_dialogs.xml.h:22
msgid "Active indicator:"
msgstr "活动指标："

#: ../src/_dialogs.xml.h:23
msgid "Force icon size:"
msgstr "强制图标大小："

#: ../src/_dialogs.xml.h:24
msgid "Inactive indicator:"
msgstr "非活动指标："

#: ../src/_dialogs.xml.h:25
msgid "Appearance"
msgstr "外观"

#: ../src/_dialogs.xml.h:26
msgid "Switch between applications with <SUPER>+[1, 2, ...]"
msgstr "使用 <SUPER>+[1， 2， ...] 在应用程序之间切换"

#: ../src/_dialogs.xml.h:27
msgid "Switch to the last window with <SUPER>"
msgstr "使用<SUPER>切换到最后一个窗口"

#: ../src/_dialogs.xml.h:28
msgid ""
"<b>This feature is disabled.</b>\n"
"It requires X11 XInput2.0 extension which is is not provided by your system."
msgstr ""
"<b>此功能已禁用。</b>\n"
"它需要 X11 XInput2.0 扩展，而您的系统不提供该扩展。"

#: ../src/_dialogs.xml.h:30
msgid "Keyboard hotkeys"
msgstr "键盘热键"

#: ../src/_dialogs.xml.h:31
msgid "Active indicator style:"
msgstr "活动指标样式："

#: ../src/_dialogs.xml.h:32
msgid "Inactive indicator style:"
msgstr "非活动指标样式："

#: ../src/_dialogs.xml.h:33
msgid "Get indicator color from theme"
msgstr "从主题获取指示器颜色"

#: ../src/_dialogs.xml.h:34
msgid "Docklike Taskbar"
msgstr "Docklike任务栏"
```

- 编译成功后，从系统提取可用文件，语言文件这里只提取了中文

```
#!/bin/bash

mkdir -p ~/usr/share/xfce4/panel/plugins/
mkdir -p ~/usr/lib/xfce4/panel/plugins/
mkdir -p ~/usr/share/locale/zh_CN/LC_MESSAGES/
cp /usr/share/xfce4/panel/plugins/docklike.desktop ~/usr/share/xfce4/panel/plugins/
cp /usr/share/locale/zh_CN/LC_MESSAGES/xfce4-docklike-plugin.mo ~/usr/share/locale/zh_CN/LC_MESSAGES/
cp /usr/lib/xfce4/panel/plugins/libdocklike.la ~/usr/lib/xfce4/panel/plugins/
cp /usr/lib/xfce4/panel/plugins/libdocklike.so ~/usr/lib/xfce4/panel/plugins/
```