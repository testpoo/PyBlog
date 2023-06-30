title: Arch+openbox+tint2安装过程
date: 2023-06-30
category: linux
tag: openbox,tint2

[TOC]

### 1.连接网络

```
#iwctl
[iwd]# device list
[iwd]# station [device] scan
[iwd]# station [device] get-networks
[iwd]# station [device] connect [SSID]
```

### 2.更新系统时间

```
# timedatectl set-ntp true 
```

### 3.建立硬盘分区

```
# fdisk -l
# cfdisk /dev/sda
```

### 4.格式化分区

```
# mkfs.fat -F 32 /dev/sda1   --boot分区
# mkfs.ext4 /dev/sda2  --根分区
# mkswap /dev/sda3  --交换空间分区
```

### 5.挂载分区

```
mount /dev/sda2 /mnt
mkdir /mnt/boot
mount /dev/sda1 /mnt/boot
swapon /dev/sda3
```

### 6.安装必需的软件包

```
# 换源：reflector -c China -a 6 --sort rate --save /etc/pacman.d/mirrorlist
# 检查硬盘：lsblk
# 安装系统：pacstrap /mnt base linux linux-firmware
```

### 7.配置系统

```
# 生成 fstab 文件: genfstab -U /mnt >> /mnt/etc/fstab
# 切换到新系统: arch-chroot /mnt
# 修改时区: ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# 时间同步: hwclock --systohc
```

### 8.本地化

- 编辑 /etc/locale.gen，然后取消掉 en_US.UTF-8 UTF-8, zh_CN.UTF-8 UTF-8前面的`#`号
- 然后执行 `locale-gen`
- 然后创建/etc/locale.conf,添加LANG=en_US.UTF-8,中文需要zh_CN.UTF-8

### 9.网络配置

```
# /etc/hosts添加以下内容
/etc/hostname  arch
/etc/hosts
127.0.0.1 localhost
::1       localhost
127.0.0.1 arch.localdomain arch
```

### 10.修改root密码

```
# passwd
```

### 11.安装引导程序

```
# pacman -S grub efibootmgr
# grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=GRUB
# grub-mkconfig -o /boot/grub/grub.cfg
```

### 12.创建用户

```
# useradd -m -G wheel poo
# useradd poo
# passwd poo
```

### 6. 安装软件

```
pacman -S xorg-server install openbox obconf tint2 sakura pcmanfm ristretto fcitx-rime librime-data-wubi lxappearance xarchiver pulseaudio blueman sudo git intel-microcode fonts-noto-cjk slock light jgmenu chromium chromium-l10n webext-ublock-origin-chromium
```

### 7.附录

#### 7.1 安装deepin

```
pacman -S xorg-server lightdm networkmanager deepin deepin-extra
systemctl enable lightdm
systemctl enable NetworkManager
```

#### 7.2 安装xfce4

```
pacman -S xfce4 xfce4-goodies nano sudo lightdm lightdm-gtk-greeter networkmanager xf86-video-intel network-manager-applet alsa-utils pulseaudio pulseaudio-alsa pavucontrol

声音问题
sudo pacman -S alsa-utils
sudo pacman -S pulseaudio
sudo pacman -S pulseaudio-alsa
sudo pacman -S pavucontrol      #与xfce4 panel里面的插件配合使用,必须要有这个进程
```

#### 7.3 网络问题

```
# 安装nm: pacman -S networkmanager
# 安装nm图形界面: nm-connection-editor
# 安装nm系统托盘图标: network-manager-applet（nm-applet）
# 开机启动nm: systemctl enable NetworkManager
```

#### 7.4 nm连接网络命令

```
nmcli 示例
显示附近的 Wi-Fi 网络：

$ nmcli device wifi list
连接到 Wi-Fi 网络：

$ nmcli device wifi connect SSID_或_BSSID password 密码
连接到隐藏的 Wi-Fi 网络：

$ nmcli device wifi connect SSID_或_BSSID password 密码 hidden yes
连接到 wlan1 网络接口上的 Wi-Fi：

$ nmcli device wifi connect SSID_或_BSSID password 密码 ifname wlan1 profile_name
断开网络接口上的连接：

$ nmcli device disconnect ifname eth0
显示连接列表及其名称、UUID、类型和支持设备：

$ nmcli connection show
激活连接（即使用现有配置文件连接到网络）：

$ nmcli connection up name_或_uuid
删除连接：

$ nmcli connection delete name_或_uuid
显示所有网络设备及其状态：

$ nmcli device
关闭 Wi-Fi：

$ nmcli radio wifi off
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

### 8. 去掉开机启动项停留的5秒和电池的问题

```
nano /etc/default/grub
找到 GRUB_DEFAULT=x,并将x改为希望启动系统的序号,默认 x == 0，即默认启动项是 Debian,启动项从上往下数分别是 0 、 1 、 2 。。。
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

### 9. 安装输入法

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

### 10. 触摸板修改

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

### 11. 设置dpi

```
nano .Xresources

Xft.dpi:120
sudo xrdb ~/.Xresources
reboot
```

### 12. 启动i3/OpenBox

编辑（不存在即新建）文件~/.bash_profile（在tty下登录是不会执行.bashrc的），新增一行内容如下：

```
if [ -z $DISPLAY ] && [ $(tty) = "/dev/tty1" ];then
    startx
fi
# 查看Ctrl-Alt-F1对应的那个tty
echo $(tty)
```

### 13. 设置

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

### 14. 详细配置文件

`https://github.com/testpoo/obconfig`