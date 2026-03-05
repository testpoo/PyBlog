title: Arch通过archinstall安装过程
date: 2026-03-05
category: 系统安装
tag: archinstall, kde, sway, labwc

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
```

### 3.安装aur软件

```
aur地址：https://aur.archlinux.org/packages

git clone [package URL]
cd [package name]
makepkg -si
```

### 4.添加Arch Linux CN 软件仓库源

```
# 在/etc/pacman.conf文件最后面添加
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

# 然后安装archlinuxcn-keyring
pacman -Sy archlinuxcn-keyring
```

### 5.pacman命令

`pacman` 是 `Arch Linux` 的包管理器。它将一个简单的二进制包格式和易用的构建系统结合了起来。不管软件包是来自官方的 `Arch` 库还是用户自己创建，`pacman` 都能方便得管理。

#### 5.1.更新系统

在 `Archlinux` 中，使用一条命令即可对整个系统进行更新：`pacman -Syu`

如果你已经使用 `pacman -Sy` 将本地的包数据库与远程的仓库进行了同步，也可以只执行：`pacman -Su`

#### 5.2.安装包

- `pacman -S` 包名：例如，执行 `pacman -S firefox` 将安装 `Firefox`。你也可以同时安装多个包，只需以空格分隔包名即可。
- `pacman -Sy` 包名：与上面命令不同的是，该命令将在同步包数据库后再执行安装。
- `pacman -Sv` 包名：在显示一些操作信息后执行安装。
- `pacman -U` 包名：安装本地包，其扩展名为 pkg.tar.gz。
- `pacman -U http://www.example.com/repo/example.pkg.tar.xz` 安装一个远程包（不在 `pacman` 配置的源里面）

#### 5.3.删除包

- `pacman -R` 包名：该命令将只删除包，保留其全部已经安装的依赖关系
- `pacman -Rs` 包名：在删除包的同时，删除其所有没有被其他已安装软件包使用的依赖关系
- `pacman -Rsc` 包名：在删除包的同时，删除所有依赖这个软件包的程序
- `pacman -Rd` 包名：在删除包时不检查依赖。

#### 5.4.搜索包

- `pacman -Ss` 关键字：在仓库中搜索含关键字的包。
- `pacman -Qs` 关键字： 搜索已安装的包。
- `pacman -Qi` 包名：查看有关包的详尽信息。
- `pacman -Ql` 包名：列出该包的文件。

#### 5.5.其他用法

- `pacman -Sw` 包名：只下载包，不安装。
- `pacman -Sc`：清理未安装的包文件，包文件位于 `/var/cache/pacman/pkg/` 目录。
- `pacman -Scc`：清理所有的缓存文件。

### 6.安装KDE

```
# 安装的软件
pacman -S fcitx5-im fcitx5-rime rime-wubi git firefox packagekit-qt6 sweeper gwenview spectacle firefox-ublock-origin fuse2 speech-dispatcher wqy-zenhei

# 向日葵启动前执行
systemctl start runsunloginclient.service

```

### 7. 安装Sway

#### 7.1. 安装Sway及相关软件
```
# 通过arch安装sway

sudo pacman -S thunar chromium gvfs fcitx5 fcitx5-rime xarchiver git upower blueman thunar-archive-plugin wl-clipboard rime-wubi ristretto libreoffice-fresh man-db 7zip xfce4-appfinder libreoffice-fresh-zh-cn

sudo pacman -Rns lightdm lightdm-gtk-greeter htop smartmontools vim waybar wget wireless_tools wpa_supplicant pavucontrol wmenu
```

#### 7.2. 输入法环境变量设置

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

#### 7.3. 启动Sway

```
# 编辑 ~/.bash_profile加入以下内容即可：

[ "$(tty)" = "/dev/tty1" ] && exec sway
```

#### 7.4. 配置sway

```
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/

# 编辑~/.config/sway
```

#### 7.5. 设置终端(foot)字体大小

```
cp -r /etc/foot/ ~/.config/foot/
vi ~/.config/foot/foot.ini

font=FreeMono:size=12
```

### 8. 安装Labwc

#### 8.1 安装Labwc及相关软件

```
sudo pacman -S chromium thunar gvfs xarchiver thunar-archive-plugin xfce4-panel xfce4-genmon-plugin foot fcitx5 fcitx5-rime rime-wubi git blueman wl-clipboard ristretto libreoffice-fresh libreoffice-fresh-zh-cn man-db 7zip swaybg swayidle swaylock wlr-randr brightnessctl wlopm mako upower grim slurp wtype

# 可选:cmus mp3插件, Motrix需要, 微信需要, 图标
cmus libmad fuse xcb-util-image tela-circle-icon-theme-blue

sudo pacman -Rns alacritty htop smartmontools vim wget wireless_tools wpa_supplicant lightdm lightdm-gtk-greeter
```

#### 8.2. 启动Labwc

```
# 编辑 ~/.bash_profile加入以下内容即可：

[ "$(tty)" = "/dev/tty1" ] && exec labwc
```

#### 8.3.设置 Fcitx5 初始配置

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

#### 8.4. iwd无法联网

```
sudo nano /etc/iwd/main.conf

[General]
EnableNetworkConfiguration=true

sudo systemctl enable iwd.service --now
sudo systemctl enable systemd-resolved.service --now
systemctl restart iwd
```

#### 8.5. 其他

```
# 若 polkit 未安装在您的系统上，并且您想使用 seatd 来替代，请将您添加到 seat 用户组并启用/启动 seatd.service，然后重新登录。
sudo systemctl enable seatd --now
sudo usermod -aG seat poo

# 通过wtype关联labwc root-menu，通过xfce启动器实现
名称：Arch程序菜单  命令：wtype -M logo -k s

# 强制xfce4-panel所有插件以内部方式运行
xfconf-query -c xfce4-panel -p /force-all-internal -t bool -s true --create

# 安装Motrix appimage包，需要安装依赖 fuse；安装微信appimage包，需要安装依赖xcb-util-image。

# libreoffice 护眼色：C7EDCC

# 解决 Chromium 浏览器卡顿缓慢的问题（在抖音和B站放视频页面卡住），禁用GPU加速：
1. 打开 Chromium 浏览器，进入“设置 → 系统”，将 使用图形加速功能 的选项关闭掉，重启浏览器。如果设置后卡顿已有明显改善，那么就此搞定，不然继续第二步。
2. 在地址栏上输入：chrome://flags/ 回车，在顶部搜索栏中搜索“gpu”，列表中找到：“GPU rasterization”(GPU 渲染) 以及 “Accelerated 2D canvas”(2D 图形加速) 两项，将它们都设为“Disabled”禁用即可。点击右下角的“ReLaunch”重启浏览器。

# 查字体
fc-list :lang=zh
fc-match
fc-match -a | grep Mono  # 等线字体

# libreoffice问题
# libreoffice打开提示错误，加载libswlo.so失败，使用下面的命令查找缺失的程序，然后安装
ldd /usr/lib/libreoffice/program/libswlo.so | grep "not found"
```