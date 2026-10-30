title: Arch通过archinstall安装过程
date: 2026-10-30
category: 系统安装
tag: xfce, kde, sway, labwc

[TOC]

### 1.连接网络

```
#iwctl
[iwd]# device list
[iwd]# station [device] scan
[iwd]# station [device] get-networks
[iwd]# station [device] connect [SSID]
```

### 2.archinstall安装

```
# 根据提示安装系统
archinstall

# 如果执行速度慢，可以换源
reflector -c China -a 6 --sort rate --save /etc/pacman.d/mirrorlist
```

### 3.添加Arch Linux CN 软件仓库源

```
# 在/etc/pacman.conf文件最后面添加
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

# 然后安装archlinuxcn-keyring
pacman -Sy archlinuxcn-keyring
```

### 4. 安装xfce

#### 4.1. 安装xfce及相关软件

```
# 安装的软件
sudo pacman -S firefox libreoffice-fresh libreoffice-fresh-zh-cn git firefox-ublock-origin fcitx5 fcitx5-rime rime-wubi blueman qogir-icon-theme-git wqy-zenhei xfce4-docklike-plugin

# PooMusic需要
gst-plugins-good python-mutagen

# 微信需要
xcb-util-image xcb-util-renderutil xcb-util-wm

# sublime输入需要
fcitx5-gtk fcitx5-qt

# 卸载的软件
sudo pacman -Rns htop xfburn vim parole xfce4-sensors-plugin xfce4-notes-plugin xfce4-dict xfce4-sensors-plugin xfce4-notes-plugin xfce4-dict xfce4-whiskermenu-plugin xfce4-weather-plugin xfce4-wavelan-plugin xfce4-verve-plugin xfce4-timer-plugin xfce4-smartbookmark-plugin xfce4-cpufreq-plugin xfce4-cpugraph-plugin xfce4-diskperf-plugin xfce4-battery-plugin xfce4-systemload-plugin xfce4-xkb-plugin xfce4-netload-plugin xfce4-mailwatch-plugin xfce4-clipman-plugin xfce4-fsguard-plugin xfce4-genmon-plugin xfce4-eyes-plugin xfce4-mount-plugin xfce4-mpc-plugin xfce4-time-out-plugin
```

#### 4.2. 输入法环境变量设置

**ibus**

添加ibus登录时启动：`ibus-daemon -rxRd`

```
nano /etc/environment

GTK_IM_MODULE=ibus
QT_IM_MODULE=ibus
XMODIFIERS="@im=ibus"
```

**fcitx**

启用fcitx输入需要配置环境变量：
```
nano /etc/environment

GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS="@im=fcitx"
```

#### 4.3. Lightdm配置

`sudo nano /etc/lightdm/lightdm-gtk-greeter.conf`

```
icon-theme-name = Qogir-Light
font-name = WenQuanYi Zen Hei Mono 10
default-user-image = #distributor-logo-archlinux
clock-format = %A %F %H:%M 第%V周
background = /usr/share/backgrounds/background.png
xft-dpi = 120
indicators = ~host;~spacer;~clock;~spacer;~a11y;~session;~power
#hide-user-image = true
```

#### 4.4. 添加gtk.css

- 路径`~/config/gtk-3.0/gtk.css`

```
#docklike-plugin button {
    padding-left: 2px;
    padding-right: 2px;
}
```

### 5.安装KDE

```
# 安装的软件
pacman -S fcitx5-im fcitx5-rime rime-wubi git firefox packagekit-qt6 sweeper gwenview spectacle firefox-ublock-origin fuse2 speech-dispatcher wqy-zenhei

# 向日葵启动前执行
systemctl start runsunloginclient.service
```

### 6. 安装Sway

#### 6.1. 安装Sway及相关软件
```
# 通过arch安装sway

sudo pacman -S thunar chromium gvfs fcitx5 fcitx5-rime xarchiver git upower blueman thunar-archive-plugin wl-clipboard rime-wubi ristretto libreoffice-fresh man-db 7zip xfce4-appfinder libreoffice-fresh-zh-cn

sudo pacman -Rns lightdm lightdm-gtk-greeter htop smartmontools vim waybar wget wireless_tools wpa_supplicant pavucontrol wmenu
```

#### 6.2. 输入法环境变量设置

启用fcitx输入需要配置环境变量：
```
nano /etc/environment

XIM="fcitx"
#GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS="@im=fcitx"
INPUT_METHOD=fcitx
SDL_IM_MODULE=fcitx
GLFW_IM_MODULE=fcitx
```

#### 6.3. 启动Sway

```
# 编辑 ~/.bash_profile加入以下内容即可：

[ "$(tty)" = "/dev/tty1" ] && exec sway
```

#### 6.4. 配置sway

```
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/

# 编辑~/.config/sway
```

#### 6.5. 设置终端(foot)字体大小

```
cp -r /etc/xdg/foot/foot.ini ~/.config/foot/
vi ~/.config/foot/foot.ini

font=FreeMono:size=12
```

### 7. 安装Labwc

#### 7.1 安装Labwc及相关软件

```
sudo pacman -S firefox firefox-ublock-origin thunar gvfs xarchiver thunar-archive-plugin xfce4-panel xfce4-appfinder xfce4-terminal fcitx5 fcitx5-rime rime-wubi git wl-clipboard ristretto libreoffice-fresh libreoffice-fresh-zh-cn man-db 7zip swaybg swayidle swaylock wlr-randr brightnessctl wlopm mako grim slurp qogir-icon-theme-git upower

PooMusic: python-mutagen gst-plugins-good
WeChat: xcb-util-image

sudo pacman -Rns alacritty htop smartmontools vim wget lightdm lightdm-gtk-greeter
```

#### 7.2. 启动Labwc

```
# 编辑 ~/.bash_profile加入以下内容即可：

[ "$(tty)" = "/dev/tty1" ] && exec labwc
```

#### 7.3.设置 Fcitx5 初始配置

配置 Group 直接启动 fcitx5 是只有西文键盘的，把下面的内容粘贴到 ~/.config/fcitx5/profile
```
[Groups/0]
# Group Name
Name=Default
# Layout
Default Layout=us
# Default Input Method
DefaultIM=rime

[Groups/0/Items/0]
# Name
Name=rime
# Layout
Layout=

[GroupOrder]
0=Default
```
DefaultIM=xx 为设置默认输入法，后面的Group中的Name为具体的输入法名字，按0，1，2……这样的编号排序，修改文件时，在要fcitx5关闭状态下，否则修改不生效。

#### 7.4. iwd无法联网

```
# 当前不需要设置了，可以直接使用
sudo nano /etc/iwd/main.conf

[General]
EnableNetworkConfiguration=true

sudo systemctl enable iwd.service --now
sudo systemctl enable systemd-resolved.service --now
systemctl restart iwd
```

#### 7.5. 其他

```
# 禁用声卡
/home/poo/.local/state/wireplumber/default-profile
[default-profile]
alsa_card.pci-0000_00_1f.3=off

# 替换thunar自带的设为壁纸
# 删除原来的设为壁纸
sudo mv /usr/lib/thunarx-3/thunar-wallpaper-plugin.so /usr/lib/thunarx-3/thunar-wallpaper-plugin.so.bak

# thunar: 编辑-->配置自定义动作
名称：设为壁纸
命令：/home/poo/.config/labwc/settings.sh change-swaybg %f
图标：preferences-desktop-wallpaper

# libreoffice 护眼色：#C7EDCC

# 查字体
fc-list :lang=zh
fc-match
fc-match -a | grep Mono  # 等线字体
```

### 8.安装aur软件

```
aur地址：https://aur.archlinux.org/packages

git clone [package URL]
cd [package name]
makepkg -si
```

### 9.pacman命令

`pacman` 是 `Arch Linux` 的包管理器。

#### 9.1.系统更新

```
# 更新所有已安装的软件包
sudo pacman -Syu

# 仅更新软件包数据库(不实际更新软件)
sudo pacman -Sy
```

#### 9.2.软件包安装

```
# 安装单个软件包
sudo pacman -S 包名

# 安装多个软件包
sudo pacman -S 包名1 包名2 包名3

# 安装本地软件包文件(不处理依赖)
sudo pacman -U /路径/到/包名.pkg.tar.zst
```

#### 9.3.软件包删除

```
# 删除软件包但保留其依赖
sudo pacman -R 包名

# 删除软件包及其不再需要的依赖
sudo pacman -Rs 包名

# 删除软件包及其所有配置文件
sudo pacman -Rns 包名
```

#### 9.4.软件包查询

```
# 搜索软件包(名称和描述)
pacman -Ss 关键词

# 列出已安装的软件包
pacman -Q

# 查询某个文件属于哪个软件包
pacman -Qo /路径/到/文件

# 显示软件包详细信息
pacman -Qi 包名
```

#### 9.5.清理缓存

```
# 清理未安装软件包的缓存
sudo pacman -Sc

# 清理所有软件包的缓存(包括已安装的)
sudo pacman -Scc
```