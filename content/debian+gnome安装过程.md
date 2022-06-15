title: debian+gnome安装过程
date: 2021-04-08
category: debian
tag: gnome

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

`sudo apt install intel-microcode fonts-noto-cjk arc-theme git ibus-rime librime-data-wubi`

### 8. 删除不需要软件

`apt autoremove --purge evolution libreoffice* gnome-calendar cheese gnome-chess gnome-clocks gnome-contacts evolution five-or-more four-in-a-row hitori gnome-klotski lightsoff gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles quadrapassel gnome-robots gnome-sudoku swell-foop tali gnome-taquin gnome-tetravex gnome-todo totem gnome-2048 gnome-weather goldendict rhythmbox shotwell simple-scan synaptic termit transmission-gtk yelp zhcon aisleriot iagno gnome-sound-recorder fcitx5*`

### 9. 设置

- 暂无

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

### 12. 安装输入法

```
sudo apt install ibus-rime librime-data-wubi
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

### 13. 删除多余的扩展

- 删除/usr/share/gnome-shell/extensions下除user-theme以外的所有扩展