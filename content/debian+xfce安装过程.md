title: debian+xfce安装过程
date: 2021-04-08
category: debian
tag: xfce

[TOC]

### 1. 下载链接

https://www.debian.org/download

### 2. 下载驱动

https://mirrors.tuna.tsinghua.edu.cn/debian-nonfree/firmware/bullseye/current/firmware.zip

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
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-updates main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ bullseye-backports main contrib non-free
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security bullseye-security main contrib non-free
```

### 7. 安装软件

```
# sudo apt install filezilla stacer meld uget aria2 intel-microcode fonts-noto-cjk arc-theme moka-icon-theme
sudo apt install filezilla stacer meld intel-microcode fonts-noto-cjk arc-theme git fcitx-rime librime-data-wubi gvfs-backends papirus-icon-theme blueman catfish drawing
```

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
https://packages.debian.org/bullseye/firmware-misc-nonfree
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

### 18. 设置xfce样式

```
~/.config/gtk-3.0/gtk.css
#pulseaudio-button image,#xfce4-power-manager-plugin image,#xfce4-notification-plugin image,#showdesktop-button image{
    -gtk-icon-transform: scale(0.4);
}
```

### 19. 修改grub背景

```
/usr/share/desktop-base/homeworld-theme/grub/grub_background.sh
WALLPAPER=/usr/share/backgrounds/background.png
注：必须是png格式
```

### 20. 添加右键

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

### 21. thunar侧边栏添加位置

- 点击文件右键`send to-->Side Panel`

### 22. 启动花屏

```
xfwm4-->vblank_mode=off
```

### 23. 安装xfce4-docklike-plugin

- 安装xfce4-docklike-plugin合并启动器和窗口管理器