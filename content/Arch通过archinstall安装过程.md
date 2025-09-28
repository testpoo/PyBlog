title: Arch通过archinstall安装过程
date: 2024-06-15
category: 系统安装
tag: linux, arch, archinstall

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

sudo pacman -S thunar chromium gvfs fcitx5 fcitx5-rime xarchiver git upower blueman thunar-archive-plugin wl-clipboard rime-wubi ristretto libreoffice man-db 7zip xfce4-appfinder libreoffice-fresh-zh-cn

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

### 7.6.添加Arch Linux CN 软件仓库源

```
# 在/etc/pacman.conf文件最后面添加
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

# 然后安装archlinuxcn-keyring
pacman -Sy archlinuxcn-keyring
```