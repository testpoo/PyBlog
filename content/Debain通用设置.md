title:Debain通用设置
date:2019-11-14
category:debian
tag:软件, linux

[TOC]

### 1. 通用设置

#### 1.1. 下载特殊版本链接

- [无驱动稳定版debian-11.5.0-amd64-netinst.iso](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.5.0-amd64-netinst.iso)

- [无驱动测试版debian-testing-amd64-netinst.iso](https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/debian-testing-amd64-netinst.iso)

- [有驱动稳定版firmware-11.5.0-amd64-netinst.iso](https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/current/amd64/iso-cd/firmware-11.5.0-amd64-netinst.iso)

- [有驱动测试版firmware-testing-amd64-netinst.iso](https://cdimage.debian.org/cdimage/unofficial/non-free/cd-including-firmware/weekly-builds/amd64/iso-cd/firmware-testing-amd64-netinst.iso)

#### 1.2. 下载驱动

<https://mirrors.tuna.tsinghua.edu.cn/debian-nonfree/firmware/bookworm/current/firmware.zip>

#### 1.3. 制作自启动U盘

`dd if=xxx.iso of=/dev/disk`

#### 1.4. 安装

#### 1.5. 将当前用户加入sudo

```
# 方法一
su root
nano /etc/sudoers添加 username ALL=(ALL:ALL) ALL

# 方法二
useradd -a -G sudo username
reboot
```

#### 1.6. 去掉debain开机启动项停留的5秒和电池的问题

```
nano /etc/default/grub
找到 GRUB_DEFAULT=x,并将x改为希望启动系统的序号,默认 x == 0，即默认启动项是 Debian,启动项从上往下数分别是 0 、 1 、 2 。。。
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

#### 1.7. 修改源

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

#### 1.8. 缺少驱动

```
# 添加驱动
https://packages.debian.org/bookworm/firmware-misc-nonfree
```

#### 1.9. 安装输入法

- fcitx-rime

```
sudo apt install fcitx-rime librime-data-wubi
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

### 2. i3/OpenBox中的通用设置

#### 2.1. 触摸板修改

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

#### 2.2. 设置dpi

```
nano .Xresources

Xft.dpi:120
sudo xrdb ~/.Xresources
reboot
```

#### 2.3. 连接wifi

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

#### 2.4. 启动i3/OpenBox

编辑（不存在即新建）文件~/.bash_profile（在tty下登录是不会执行.bashrc的），新增一行内容如下：

```
if [ -z $DISPLAY ] && [ $(tty) = "/dev/tty1" ];then
    startx
fi
# 查看Ctrl-Alt-F1对应的那个tty
echo $(tty)
```