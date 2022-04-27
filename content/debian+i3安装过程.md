title: debian+i3安装过程
date: 2021-04-08
category: debian
tag: i3

[TOC]

### 1. 连接wifi

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

- 启动网卡：`ifup wlp1s0`

### 2. 安装软件

```
apt install i3 xinit sakura rofi thunar feh fcitx-rime librime-data-wubi lxappearance xarchiver pulseaudio blueman thunar-archive-plugin deepin-screenshot neofetch ristretto intel-microcode fonts-noto-cjk

# 安装xinit  X服务
# i3 平铺式桌面管理器
# sakura 终端
# rofi 程序查找
# thunar 文件管理区
# feh 背景设置
# fcitx-rime 输入法
# lxappearance 设置字体主题
# xarchiver 解压缩
# pulseaudio 声卡驱动 默认是静音，需要打开静音，然后才有声音
# blueman 蓝牙 # 其附带的托盘工具名为blueman-applet
# thunar-archive-plugin thunar右键添加“压缩/解压”菜单
# deepin-screenshot 截图
# neofetch 系统信息
# ristretto 图片查看器
```

### 3. 启动i3

编辑（不存在即新建）文件~/.bash_profile（在tty下登录是不会执行.bashrc的），新增一行内容如下：

```
if [ -z $DISPLAY ] && [ $(tty) = "/dev/tty1" ];then`
    startx
fi
# 查看Ctrl-Alt-F1对应的那个tty
echo $(tty)
```

### 4. 配置文件地址

```
~./config/i3/config
~./config/i3status/config
```

### 5. rofi配置

```
mkdir -p ~/.config/rofi
rofi -dump-config > ~/.config/rofi/config.rasi
drun-icon-theme: "MY_ICON_THEME";
```

### 6. 亮度调节

```
# xorg-xbacklight 亮度调节
bindsym XF86MonBrightnessUp exec light -A 5 # increase screen brightness
bindsym XF86MonBrightnessDown exec light -U 5 # decrease screen brightness

bindsym XF86MonBrightnessUp exec light -A 10 && killall -SIGUSR1 i3status
bindsym XF86MonBrightnessDown exec light -U 10 && killall -SIGUSR1 i3status
# 如果没有killall命令，安装psmisc
```

### 7. 触摸板修改

```
/usr/share/X11/xrog.conf.d/40-libinput.conf

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

### 8. 字符图标

```
http://www.fontawesome.com.cn/cheatsheet/
```

### 9. 设置dpi

```
nano .Xresources

Xft.dpi:120
sudo xrdb ~/.Xresources
reboot
```

### 10. 添加休眠和锁屏

```
exec --no-startup-id xset dpms 333 666
系统闲置333秒后灭屏，666秒后系统挂起。
```

### 11. 设置锁屏背景

```
bindsym l exec --no-startup-id i3lock i3clock -i ~/.poo/i3lock.png
exec --no-startup-id xss-lock --transfer-sleep-lock -- i3lock --nofork -i ~/.poo/i3lock.png
```

### 12. 消息通知和蓝牙

```
exec --no-startup-id dunst
exec --no-startup-id blueman-applet
```

### 13. 分配到某个虚拟空间

```
for_windwo [title="poo@debian: ~"] move to workspace 1
assign [class="X-terminal-emulator"] 1

# 注：可以通过xprop来获取类名，sublime不支持，官方解释软件未开源，无法支持
```

### 14. 我的配置

<https://github.com/testpoo/i3config>

### 99.桌面插件Conky

```
https://www.cnblogs.com/LungGiyo/p/6019412.html
https://www.lifewire.com/beginners-guide-to-conky-4043352
展示在桌面：own_window_type override
```