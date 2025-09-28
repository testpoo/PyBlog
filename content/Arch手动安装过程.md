title: Arch手动安装过程
date: 2023-06-30
category: 系统安装
tag: deep, xfce

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

### 6. 安装桌面/WM

#### 6.1 安装openbox

```
pacman -S xorg-xinit install openbox obconf tint2 sakura pcmanfm ristretto fcitx-rime librime-data-wubi lxappearance xarchiver pulseaudio blueman sudo git intel-microcode fonts-noto-cjk slock light jgmenu chromium chromium-l10n webext-ublock-origin-chromium
```

#### 6.2 安装deepin

```
pacman -S xorg-server lightdm networkmanager deepin deepin-extra
systemctl enable lightdm
systemctl enable NetworkManager
```

#### 6.3 安装xfce4

```
pacman -S xfce4 xfce4-goodies nano sudo lightdm lightdm-gtk-greeter networkmanager xf86-video-intel network-manager-applet alsa-utils pulseaudio pulseaudio-alsa pavucontrol

声音问题
sudo pacman -S alsa-utils
sudo pacman -S pulseaudio
sudo pacman -S pulseaudio-alsa
sudo pacman -S pavucontrol      #与xfce4 panel里面的插件配合使用,必须要有这个进程
```

### 7 网络问题

```
# 安装nm: pacman -S networkmanager
# 安装nm图形界面: nm-connection-editor
# 安装nm系统托盘图标: network-manager-applet（nm-applet）
# 开机启动nm: systemctl enable NetworkManager
```

### 8. nm连接网络命令

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
