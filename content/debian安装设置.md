title: debian安装设置
date: 2025-09-28
category: 系统安装
tag: gnome, xfce, kde, sway, labwc, wayfire

[TOC]

### 1. 下载链接

- [稳定版：https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/)

- [测试版：https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/](https://cdimage.debian.org/cdimage/weekly-builds/amd64/iso-cd/)

### 2. 制作自启动U盘

`dd if=xxx.iso of=/dev/disk`

### 3. 将当前用户加入sudo

```
# 方法一
su root
nano /etc/sudoers添加 username ALL=(ALL:ALL) ALL

# 方法二
useradd -a -G sudo username
reboot
```

### 4. 去掉debain开机启动项停留的5秒和电池的问题

```
# 使用grup时使用，使用systemd-boot请忽略

nano /etc/default/grub
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

### 5. 修改源

<https://mirrors.tuna.tsinghua.edu.cn/help/debian/>

- 传统格式（/etc/apt/sources.list）

```
# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ testing main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ testing main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ testing-updates main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ testing-updates main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian/ testing-backports main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian/ testing-backports main contrib non-free non-free-firmware
deb https://mirrors.tuna.tsinghua.edu.cn/debian-security testing-security main contrib non-free non-free-firmware
# deb-src https://mirrors.tuna.tsinghua.edu.cn/debian-security testing-security main contrib non-free non-free-firmware
# deb https://security.debian.org/debian-security testing-security main contrib non-free non-free-firmware
# # deb-src https://security.debian.org/debian-security testing-security main contrib non-free non-free-firmware
```

- DEB822 格式（/etc/apt/sources.list.d/debian.sources）

```
Types: deb
URIs: https://mirrors.tuna.tsinghua.edu.cn/debian
Suites: testing testing-updates testing-backports
Components: main contrib non-free non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

# 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
# Types: deb-src
# URIs: https://mirrors.tuna.tsinghua.edu.cn/debian
# Suites: testing testing-updates testing-backports
# Components: main contrib non-free non-free-firmware
# Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

# 以下安全更新软件源包含了官方源与镜像站配置，如有需要可自行修改注释切换
Types: deb
URIs: https://mirrors.tuna.tsinghua.edu.cn/debian-security
Suites: testing-security
Components: main contrib non-free non-free-firmware
Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg

# Types: deb-src
# URIs: https://mirrors.tuna.tsinghua.edu.cn/debian-security
# Suites: testing-security
# Components: main contrib non-free non-free-firmware
# Signed-By: /usr/share/keyrings/debian-archive-keyring.gpg
```

### 6. Gnome桌面设置

#### 6.1 安装软件

`sudo apt install intel-microcode fonts-noto-cjk git ibus-rime rime-data-wubi`

#### 6.2. 删除不需要软件

`apt autoremove --purge evolution libreoffice* gnome-calendar cheese gnome-chess gnome-clocks gnome-contacts evolution five-or-more four-in-a-row hitori gnome-klotski lightsoff gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles quadrapassel gnome-robots gnome-sudoku swell-foop tali gnome-taquin gnome-tetravex gnome-todo totem gnome-2048 gnome-weather goldendict rhythmbox shotwell simple-scan synaptic termit transmission-gtk yelp zhcon aisleriot iagno gnome-sound-recorder fcitx5*`

#### 6.3. 删除多余的扩展

- 删除/usr/share/gnome-shell/extensions下除user-theme以外的所有扩展

### 7. xfce桌面设置

#### 7.1. 删除软件

`sudo apt autoremove libreoffice* exfalso parole quodlibet synaptic xfburn xterm xfce4-whiskermenu-plugin xfce4-weather-plugin xfce4-wavelan-plugin xfce4-verve-plugin xfce4-timer-plugin xfce4-smartbookmark-plugin xfce4-cpufreq-plugin xfce4-cpugraph-plugin xfce4-diskperf-plugin xfce4-battery-plugin xfce4-sensors-plugin xfce4-systemload-plugin xfce4-xkb-plugin xfce4-netload-plugin xfce4-mailwatch-plugin xfce4-clipman-plugin xfce4-fsguard-plugin atril xfce4-genmon-plugin xsane --purge`

#### 7.2. 安装软件

`sudo apt install ibus git ibus-rime rime-data-wubi gvfs-backends blueman yaru-theme-gtk fonts-noto-cjk webext-ublock-origin-firefox ristretto xfce4-screenshooter xfce4-taskmanager xfce4-docklike-plugin pkexec pipewire-audio firefox-esr-l10n-zh-cn`

可选图标 `https://github.com/vinceliuice/McMojave-circle`

#### 7.3. 设置

- 快捷键设置:设置-->键盘-->应用程度快捷键

- 窗口样式设置：设置-->窗口管理器-->样式+按钮布局

- 窗口管理器微调：设置-->窗口管理器微调-->辅助功能  最大化窗口时隐藏标题

- 窗口管理器微调：设置-->窗口管理器微调-->合成器  在dock窗口下显示阴影

- 主题/字体设置：外观-->样式+字体

- 设置时钟格式：%A %F %H:%M 第%V周 | %F%n%H:%M | %H:%M%n%Y/%m/%d


#### 7.4. 添加触摸板关启脚本

本机快捷键Fn+F8==Super+Ctrl_L

直接在键盘中设置该命令，直接打开关闭触摸板工具
```
xfce4-mouse-settings --device="SYNA3602:00 093A:0255 Touchpad"
xfce4-mouse-settings -d "SYNA3602:00 093A:0255 Touchpad"
```

#### 7.5. lightdm设置

```
/etc/lightdm/lightdm-gtk-greeter.conf
[greeter]
theme-name = Yaru
icon-theme-name = Qogir-icon
font-name = Noto Sans Mono 10
default-user-image = #distributor-logo
clock-format = %A %F %H:%M 第%V周
background = /usr/share/backgrounds/background.png
xft-dpi = 120
indicators = ~host;~spacer;~clock;~spacer;~a11y;~session;~power
#hide-user-image = true

/etc/lightdm/lightdm.conf
greeter-hide-users=false 前的#去掉
```

#### 7.6. 启动gtk编辑器

```
xfce4-panel -q && GTK_DEBUG=interactive xfce4-panel
重启xfce-panel:xfce4-panel -r
```

#### 7.7. 添加右键

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

#### 7.8. 启动花屏

```
xfwm4-->vblank_mode=off
```

#### 7.9. 添加gtk.css

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

### 8. kde桌面设置

#### 8.1. 安装软件

`sudo apt install fonts-noto-cjk git fcitx5-rime rime-data-wubi plasma-calendar-addons`

#### 8.2. 删除不需要软件

`apt autoremove --purge kmail kaddressbook korganizer okular akregator konqueror kwalletmanager k3b juk dragonplayer gimp imagemagick* kontrast kmenuedit qt5-style-kvantum kdeconnect* kmouth kmousetool kmag xterm`

#### 8.3. 安装图标主题

- 通过`https://github.com/yeyushengfan258/Win11-icon-theme`下载

- 进入`Win11-icon-theme`目录，执行`./install.sh -a`命令

#### 8.4. 安装窗口装饰

- 通过`https://github.com/vinceliuice/Colloid-kde/`下载

- 安装窗口装饰元素`Colloid-light-round`到`~/.local/share/aurorae/themes/`下

#### 8.5. 安装SDDM主题

- 通过`https://github.com/MarianArlt/kde-plasma-chili`下载

- 进入`kde-plasma-chili`目录，执行`cp -r kde-plasma-chili /usr/share/sddm/themes`命令

#### 8.6. 解决无法更换头像

- 这是账号服务的一个缺陷: 打开`sudo nano /usr/lib/systemd/system/accounts-daemon.service`文件，修改`PrivateTmp=true`为`PrivateTmp=false`，然后重启即可解决问题，这个问题已经不存在。

#### 8.7. 修改设置

- 桌面背景修改：设置-->更改壁纸-->壁纸类型：每日一图-->提供：必应

- 双击打开文件：设置-->点击文件或文件夹时-->选中他们

- 去掉程序特效：设置-->外观-->光标-->配置程序启动动效，沟选“无动效”，沟去“启动动效”。

- 去掉欢迎屏幕：设置-->外观-->欢迎屏幕选无。

- 锁屏背景修改：设置-->工作区行为-->锁屏-->配置-->壁纸类型：每日一图-->提供：必应

- 修改登录画面：设置-->开机与关机-->登录屏幕(SDDM)-->选择安装的新画面

- 修改用户头像：设置-->用户-->修改用户头像

- 触摸板设置：设置-->输入设备-->触摸板-->手指轻触

- 绽放设置：设置-->显示器配置-->全局缩放率：125% 

### 9. Sway窗口管理器设置

#### 9.1. 安装Sway及相关软件
```
sudo apt install fcitx5 fcitx5-rime rime-data-wubi thunar xarchiver pipewire-audio blueman thunar-archive-plugin fonts-noto-cjk sway swaybg swayidle swaylock foot wofi seatd xwayland grim git brightnessctl wl-clipboard slurp upower
```

#### 9.2. 启动Sway

```
# 编辑 ~/.profile加入以下内容即可：

if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
  exec sway
fi
```

#### 9.3. 配置sway

```
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/

# 编辑~/.config/sway
```

#### 9.4. 设置终端(foot)字体大小

```
cp -r /etc/foot/ ~/.config/foot/
vi ~/.config/foot/foot.ini

font=monospace:size=12
```

### 10. labwc窗口管理器设置

#### 10.1. 安装labwc及相关软件
```
sudo apt install labwc swaybg swayidle swaylock kanshi fcitx5 fcitx5-rime rime-data-wubi thunar xarchiver pipewire-audio blueman thunar-archive-plugin fonts-noto-cjk foot wofi seatd xwayland git brightnessctl firefox-esr wlopm mako-notifier
```
#### 10.2. 启动labwc
```
# 编辑 ~/.profile加入以下内容即可：

if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
  exec labwc
fi
```
#### 10.3. 添加labwc配置文件
```
mkdir -p ~/.config/labwc
cp /usr/share/doc/labwc/* ~/.config/labwc/
```
#### 10.4. 输入法环境变量设置
启用fcitx输入需要配置环境变量：
```
nano ~/.config/labwc/environment

XIM="fcitx"
#GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS="@im=fcitx"
INPUT_METHOD=fcitx
SDL_IM_MODULE=fcitx
GLFW_IM_MODULE=fcitx
```   
#### 10.5 开机启动设置
```
nano autostart

# 背景设置
swaybg -i '/home/poo/图片/3.jpg' >/dev/null 2>&1 &

fcitx5 >/dev/null 2>&1 &
blueman-applet >/dev/null 2>&1 &
```
#### 10.6. 设置终端(foot)字体大小
```
cp -r /etc/foot/ ~/.config/foot/
vi ~/.config/foot/foot.ini

font=monospace:size=12
```
#### 10.7. 设置kanshi
```
mkdir -p ~/.config/kanshi
nano config

# 缩放1.25
profile nomad {
    output eDP-1 enable scale 1.25
}
```

### 11. wayfire窗口管理器设置

#### 11.1. 安装wayfire及相关软件
```
sudo apt install wayfire swaybg swayidle swaylock fcitx5 fcitx5-rime rime-data-wubi thunar xarchiver pipewire-audio blueman thunar-archive-plugin fonts-noto-cjk xfce4-terminal xfce4-appfinder seatd xwayland git brightnessctl firefox-esr webext-ublock-origin-firefox firefox-esr-l10n-zh-cn mako-notifier grim wl-clipboard slurp libglib2.0-bin waybar chromium chromium-l10n
```

#### 11.2. 启动wayfire
```
# 编辑 ~/.profile加入以下内容即可：

if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
  exec wayfire
fi
```

#### 11.3. wayfire
```
cp /usr/share/wayfire/examples/wayfire.ini ~/.config/wayfire.ini
```

### 11.4. 输入法环境变量设置

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

### 11.5. 设置终端(foot)字体大小
```
cp -r /etc/foot/ ~/.config/foot/
vi ~/.config/foot/foot.ini

# 也可以直接在/etc/foot/foot.ini中修改
font=monospace:size=12
```

### 12. rime输入法设置

- fcitx5-rime

```
sudo apt install fcitx5-rime rime-data-wubi
nano ~/.local/share/fcitx5/rime/default.custom.yaml
patch:
  schema_list:
    - schema: wubi_pinyin
    - schema: luna_pinyin_simp
    - schema: wubi86
```

- ibus-rime

```
sudo apt install ibus-rime rime-data-wubi
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
```

- wayland下xwayland程序fcitx输入法支持，需要配置环境变量：
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