title: debian+sway安装设置
date: 2025-01-15
category: 系统安装
tag: debian, sway

[TOC]

### 1. 安装Sway及相关软件
```
sudo apt install fcitx5 fcitx5-rime rime-data-wubi thunar xarchiver pulseaudio blueman thunar-archive-plugin fonts-noto-cjk sway swaybg swayidle swaylock foot wofi seatd xwayland grim git brightnessctl wl-clipboard slurp upower

# wl-clipboard 剪切板
# slurp 截图选框
```

### 2. 输入法环境变量设置

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

### 3. 启动Sway

```
# 编辑 ~/.profile加入以下内容即可：

if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
  exec sway
fi
```

### 4. 配置sway

```
mkdir -p ~/.config/sway
cp /etc/sway/config ~/.config/sway/

# 编辑~/.config/sway
```

### 5. 修改程序启动器

```
# 注释掉$menu行，改为以下内容：
set $menu set $menu wofi -S drun -I -G -p "请输入程序名称"
```

### 6. 设置终端(foot)字体大小

```
cp -r /etc/foot/ ~/.config/foot/
vi ~/.config/foot/foot.ini

font=monospace:size=12
```

### 7. 设置分辨率和缩放

```
swaymsg -t get_outputs
output eDP-1 resolution 1920x1200 position 0,0 scale 1.25
```

### 8. 设置触摸板

```
swaymsg -t get_inputs
input "2362:597:SYNA3602:00_093A:0255_Touchpad" {
    dwt enabled
    tap enabled
    natural_scroll enabled
    middle_emulation enabled
    events enabled
}
```

### 9. Chromium支持wayland并支持fcitx5

```
--ozone-platform=wayland --enable-wayland-ime --wayland-text-input-version=3  --gtk-version=4
```

### 10. Sway配置文件修改

```
exec_always swaybg -i /home/poo/图片/2.jpg

set $menu set $menu wofi -S drun -I -G -p "请输入程序名称"

output eDP-1 resolution 1920x1200 position 0,0 scale 1.25

input "2362:597:SYNA3602:00_093A:0255_Touchpad" {
    dwt enabled
    tap enabled
    natural_scroll enabled
    middle_emulation enabled
    events enabled
}

exec_always --no-startup-id fcitx5 -d --replace
exec_always --no-startup-id blueman-applet

bindsym XF86AudioRaiseVolume exec pactl set-sink-volume @DEFAULT_SINK@ +5%;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh
bindsym XF86AudioLowerVolume exec pactl set-sink-volume @DEFAULT_SINK@ -5%;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh
bindsym XF86AudioMute exec pactl set-sink-mute @DEFAULT_SINK@ toggle;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh
bindsym XF86AudioMicMute exec pactl set-source-mute @DEFAULT_SOURCE@ toggle;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh
bindsym XF86MonBrightnessDown exec brightnessctl set 5%-;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh
bindsym XF86MonBrightnessUp exec brightnessctl set 5%+;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh

# 隐藏或者显示bar
# bar toggle, hide or show
bindsym $mod+m bar mode toggle

# 工作台切换
# switch to near workspace
bindsym $mod+Tab workspace next
bindsym $mod+Shift+Tab workspace prev

# 边框格式
# change border style
# bindsym $mod+u border none
# bindsym $mod+n border normal
# bindsym $mod+o border 1pixel
# bindsym $mod+b border toggle

# 默认设置没标题栏
default_border pixel 0

# foucus follows mouse(cursor)
focus_follows_mouse yes

set $mode_system 锁屏(l)丨退出(e)丨挂起(s)丨休眼(h)丨重启(r)丨关机(p)
mode "$mode_system" {
    bindsym l exec --no-startup-id swaylock, mode "default"
    bindsym e exec --no-startup-id swaymsg exit, mode "default"
    bindsym s exec --no-startup-id systemctl suspend, mode "default"
    bindsym h exec --no-startup-id systemctl hibernate, mode "default"
    bindsym r exec --no-startup-id systemctl reboot, mode "default"
    bindsym p exec --no-startup-id systemctl poweroff -i, mode "default"

    # back to normal: Enter or Escape
    bindsym Return mode "default"
    bindsym Escape mode "default"
}

bindsym $mod+p mode "$mode_system"

bindsym $mod+t exec Thunar
bindsym $mod+q exec firefox-esr
bindsym $mod+Control_L exec /home/poo/.config/sway/touchpad.py;exec pkill -SIGUSR1 -f /home/poo/.config/sway/bar.sh
bindsym $mod+Shift+s exec grim -g "$(slurp)" - | wl-copy
bindsym Print exec grim - | wl-copy
bindsym $mod+Shift+i exec /home/poo/.config/sway/systeminfo | wofi -d -G -s /home/poo/.config/sway/systeminfo.css -W 485 -H 530

# 设置窗口浮动
for_window [class="wechat"] floating enable
for_window [app_id="io.github.quodlibet.QuodLibet"] floating enable

# 弹窗
# popups
for_window [window_role="pop-up"] floating enable
for_window [window_role="task_dialog"] floating enable
for_window [title="文件操作进度"] floating enable
for_window [title="确认替换文件"] floating enable

#for_window [app_id="firefox-esr"] move container workspace number $ws1
#for_window [app_id="Thunar"] move container workspace number $ws2
#for_window [app_id="foot"] move container workspace number $ws3
#for_window [app_id="sublime_text"] move container workspace number $ws4
```
