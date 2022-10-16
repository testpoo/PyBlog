title: debian+openbox+tint2安装过程
date: 2022-07-18
category: debian
tag: openbox,tint2

[TOC]

### 1. 下载链接

<https://www.debian.org/download>

### 2. 下载驱动

<https://mirrors.tuna.tsinghua.edu.cn/debian-nonfree/firmware/bookworm/current/firmware.zip>

### 3. 制作自启动U盘

### 4. 安装

### 5. 连接wifi

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

### 6. 去掉debain开机启动项停留的5秒和电池的问题

```
su root
nano /etc/sudoers添加 poo ALL=(ALL:ALL) ALL
nano /etc/default/grub
找到 GRUB_DEFAULT=x,并将x改为希望启动系统的序号,默认 x == 0，即默认启动项是 Debian,启动项从上往下数分别是 0 、 1 、 2 。。。
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

### 7. 修改源

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

### 8. 安装软件

`apt install openbox xinit tint2 sakura thunar feh fcitx-rime librime-data-wubi lxappearance xarchiver pulseaudio blueman thunar-archive-plugin neofetch ristretto intel-microcode fonts-noto-cjk slock light`

```
light 亮度
slock 锁屏
neofetch 系统信息
tint2 任务栏
sakura 设置背景
lxappearance 外观
pulseaudio 声音驱动
blueman 蓝牙

# 可选
jgmenu 菜单：进程杀不死
libnotify-bin 通知
dunst 通知
volumeicon-alsa 音量控制
network-manager 网络
```

### 9. 启动openbox

编辑（不存在即新建）文件~/.bash_profile（在tty下登录是不会执行.bashrc的），新增一行内容如下：

```
if [ -z $DISPLAY ] && [ $(tty) = "/dev/tty1" ];then`
    startx
fi
# 查看Ctrl-Alt-F1对应的那个tty
echo $(tty)
```

### 10. 触摸板修改

```
/usr/share/X11/xorg.conf.d/40-libinput.conf

Section "InputClass"
        Identifier "libinput touchpad catchall"
        MatchIsTouchpad "on"
        MatchDevicePath "/dev/input/event*"
        Driver "libinput"

        Option "Tapping" "on" # 触摸以点击
        Option "ClickMethod" "clickfinger" # 触摸板不再拥有中右键区域的区分，与之代替的是双指代表右键，三指代表中键。
        Option "NaturalScrolling" "true" # 自然滚动（反方向滚动）
        Option "SendEventsMode" "disabled-on-external-mouse" # 当检测到 USB 鼠标时，它将禁用触摸板。
        Option "DisableWhileTyping" "True" # 防止打字时误触触控板
        Option "TappingDrag" "True" # 轻击后手指按住会使单个按钮关闭，此手指的所有动作都将转换为拖动动作。
#        Option "ScrollMethod" "edge" # 边缘滚动页面
EndSection
```

### 11. 字符图标

<http://www.fontawesome.com.cn/cheatsheet/>


### 12. 设置dpi

```
nano .Xresources

Xft.dpi:120
sudo xrdb ~/.Xresources
reboot
```

### 13. 设置

- openbox

```
$ mkdir -p ~/.config/openbox
$ cp /etc/xdg/openbox/{rc.xml,menu.xml,autostart,environment} ~/.config/openbox
```

```
# autostart.sh

tint2 &
fcitx &
blueman-applet &
#volumeicon &
feh --bg-scale "/home/poo/.poo/bg.jpg" &
```
```
# keyboard中加入如下代码

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
```
# menu.xml

<?xml version="1.0" encoding="UTF-8"?>

<openbox_menu xmlns="http://openbox.org/"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://openbox.org/
                file:///usr/share/openbox/menu.xsd">

<menu id="root-menu" label="Openbox 3">
  <item label="终端" icon="/usr/share/icons/Papirus-Light/24x24/apps/terminal.svg">
    <action name="Execute"><execute>x-terminal-emulator</execute></action>
  </item>
  <item label="浏览器" icon="/usr/share/icons/Papirus-Light/24x24/apps/browser.svg">
    <action name="Execute"><execute>x-www-browser</execute></action>
  </item>
  <item label="文件" icon="/usr/share/icons/Papirus-Light/24x24/apps/Thunar.svg">
    <action name="Execute"><execute>Thunar</execute></action>
  </item>
  <!-- This requires the presence of the 'obamenu' package to work -->
  <menu id="/Debian" />
  <separator />
  <menu id="applications-menu" label="程序" icon="/usr/share/icons/Papirus-Light/24x24/apps/preferences-other.svg" execute="/home/poo/.poo/obamenu.py"/>
  <separator />
  <item label="配置OpenBox" icon="/usr/share/icons/Papirus-Light/24x24/apps/preferences-theme.svg">
    <action name="Execute"><execute>obconf</execute></action>
  </item>
  <item label="重置OpenBox" icon="/usr/share/icons/Papirus-Light/24x24/apps/systemback.svg">
    <action name="Reconfigure" />
  </item>
  <item label="重启OpenBox" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-reboot.svg">
    <action name="Restart" />
  </item>
  <separator />
  <item label="退出OpenBox" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-shutdown.svg">
    <action name="Exit" />
  </item>
  <separator />
  <menu id="system-out" label="退出" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-shutdown.svg"  >
  <item label="锁屏" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-lock-screen.svg">
    <action name="Execute"><execute>slock</execute></action>
  </item>
  <item label="挂起" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-log-out.svg">
    <action name="Execute"><execute>systemctl -i suspend</execute></action>
  </item>
  <item label="休眼" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-hibernate.svg">
    <action name="Execute"><execute>systemctl -i hibernate</execute></action>
  </item>
  <item label="重启" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-reboot.svg">
    <action name="Execute"><execute>systemctl -i reboot</execute></action>
  </item>
  <item label="关机" icon="/usr/share/icons/Papirus-Light/24x24/apps/system-shutdown.svg">
    <action name="Execute"><execute>systemctl -i poweroff</execute></action>
  </item>
</menu>
</menu>

</openbox_menu>

```
```
# obamenu.py

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version 1.1.7 
# ---- config ---
applications_dirs = ("/usr/share/applications", )
image_dir_base = "/usr/share" # without "pixmaps" -/usr/local/share in FreeBSD, /usr/share on linux
icon_Theme = "Papirus"
image_cat_prefix = "applications-"  # if empty will create no icon text only menu
application_groups = ("Office",  "Development",  "Graphics", "Internet",  "Games", "System",  "Multimedia",  "Utilities",  "Settings")
application_groups_zh = ("办公",  "开发",  "图形", "互联网",  "游戏", "系统",  "多媒体",  "实用工具",  "设置")
group_aliases = {"Audio":"Multimedia","AudioVideo":"Multimedia","Network":"Internet","Game":"Games", "Utility":"Utilities", "GTK":"",  "GNOME":""}
ignoreList = ("evince-previewer", "Ted",  "wingide3.2", "python3.4", "feh","xfce4-power-manager-settings" )
terminal_string = "evte -e"    # your favourites terminal exec string
simpleOBheader = False  # print full xml style OB header
# --- End of user config ---
 
import glob

class dtItem(object):
  def __init__(self, fName):
    self.fileName = fName
    self.Name = ""
    self.Comment = ""
    self.Exec = ""
    self.Terminal = None
    self.Type = ""
    self.Icon = ""
    self.Categories = ()

  def addName(self, data):
    self.Name = xescape(data)

  def addComment(self, data):
    self.Comment = data

  def addExec(self, data):
    if len(data) > 3 and data[-2] == '%': # get rid of filemanager arguments in dt files
      data = data[:-2].strip()
    self.Exec = data

  def addIcon(self, data):
    self.Icon = ""
    if image_cat_prefix == "":
      return
    image_dir = image_dir_base + "/icons/" + icon_Theme + "/24x24/apps/"
    di = data.strip()
    if len(di) < 3:
      #"Error in %s: Invalid or no icon '%s'" % (self.fileName,  di)
      return
    dix = di.find("/")    # is it a full path?
    if dix >= 0 and dix <= 2: # yes, its a path (./path or ../path or /path ...)
      self.Icon = di
      return
    #else a short name like "myapp"
    tmp = image_dir + di + ".*"
    tmp = glob.glob(tmp)
    if len(tmp) > 0:
      self.Icon = tmp[0]
    return

  def addTerminal(self, data):
    if data == "True" or data == "true":
      self.Terminal = True
    else:
      self.Terminal = False

  def addType(self, data):
    self.Type = data

  def addCategories(self, data):
    self.Categories = data

def getCatIcon(cat):
  iconDir = image_dir_base + "/icons/" + icon_Theme + "/24x24/apps/"
  cat = image_cat_prefix + cat.lower()
  tmp = glob.glob(iconDir + cat + ".*")
  if len(tmp) > 0:
    return tmp[0]
  return ""

def xescape(s):
  Rep = {"&":"&amp;", "<":"&lt;", ">":"&gt;",  "'":"&apos;", "\"":"&quot;"}
  for p in ("&", "<", ">",  "'","\""):
    sl = len(s); last = -1
    while last < sl:
      i = s.find(p,  last+1)
      if i < 0:
        done = True
        break
      last = i
      l = s[:i]
      r = s[i+1:]
      s = l + Rep[p] + r
  return s

def process_category(cat, curCats,  appGroups = application_groups,  aliases = group_aliases ):
  # first process aliases
  if cat in aliases:
    if aliases[cat] == "":
      return ""                # ignore this one
    cat = aliases[cat]
  if cat in appGroups and cat not in curCats:  # valid categories only and no doublettes, please
    curCats.append(cat)
    return cat
  return ""


def process_dtfile(dtf,  catDict):  # process this file & extract relevant info
  active = False      # parse only after "[Desktop Entry]" line
  fh = open(dtf,  "r")
  lines = fh.readlines()
  this = dtItem(dtf)
  for l in lines:
    l = l.strip()
    if l == "[Desktop Entry]":
      active = True
      continue
    if active == False:  # we don't care about licenses or other comments
      continue
    if l == None or len(l) < 1 or l[0] == '#':
      continue
    if l[0]== '[' and l !=  "[Desktop Entry]":
      active = False
      continue
    # else
    eqi = l.split('=')
    if len(eqi) < 2:
      print("Error: Invalid .desktop line'" + l + "'")
      continue
    # Check what it is ...
    if eqi[0] == "Name[zh_CN]":
      this.addName(eqi[1])
    elif eqi[0] == "Name" and this.Name == "":
      this.addName(eqi[1])
    elif eqi[0] == "Comment":
      this.addComment(eqi[1])
    elif eqi[0] == "Exec":
      this.addExec(eqi[1])
    elif eqi[0] == "Icon":
      this.addIcon(eqi[1])
    elif eqi[0] == "Terminal":
      this.addTerminal(eqi[1])
    elif eqi[0] == "Type":
      if eqi[1] != "Application":
        continue
      this.addType(eqi[1])
    elif eqi[0] == "Categories":
      if eqi[1] and eqi[1][-1] == ';':
        eqi[1] = eqi[1][0:-1]
      cats = []
      # DEBUG 
      dtCats = eqi[1].split(';')
      for cat in dtCats:
        result = process_category(cat,  cats)
      this.addCategories(cats)
    else:
      continue
  # add to catDict
  #this.dprint()
  if len(this.Categories) > 0:    # don't care about stuff w/o category
    for cat in this.Categories:
      catDict[cat].append(this)

categoryDict = {}

if __name__ == "__main__":
  # init the application group dict (which will contain list of apps)
  for appGroup in application_groups:
    categoryDict[appGroup] = []

  # now let's look  into the app dirs ...
  for appDir in applications_dirs:
    appDir += "/*.desktop"
    dtFiles = glob.glob(appDir)

    # process each .desktop file in dir
    for dtf in dtFiles:
      skipFlag = False
      for ifn in ignoreList:
        if dtf.find(ifn) >= 0:
          skipFlag = True
      if skipFlag == False:
        process_dtfile(dtf,  categoryDict)

  # now, generate jwm menu include
  if simpleOBheader == True:
    print('<openbox_pipe_menu>')     # magic header
  else:
    print('<?xml version="1.0" encoding="UTF-8" ?><openbox_pipe_menu xmlns="http://openbox.org/"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:schemaLocation="http://openbox.org/" >')    # magic header
  appGroupLen = len(application_groups)
  for ag in range(appGroupLen ):
    catList = categoryDict[application_groups[ag]]
    if len(catList) < 1:
      continue        # don't create empty menus
    catStr = "<menu id=\"openbox-%s\" label=\"%s\" " % (application_groups[ag], application_groups_zh[ag])
    tmp = getCatIcon(application_groups[ag])
    if tmp != "":
      catStr += "icon=\"%s\"" % tmp
    else:
      catStr += "icon=\"" + image_dir_base + "/icons/" + icon_Theme + "/24x24/actions/settings.svg\""
    print(catStr,  ">")
    for app in catList:
      progStr = "<item "
      progStr += "label=\"%s\" "  % app.Name
      if app.Icon != "":
        progStr += "icon=\"%s\" " % app.Icon
      elif app.Name == "蓝牙适配器":
        progStr += "icon=\"" + image_dir_base + "/icons/" + icon_Theme + "/24x24/devices/blueman-device.svg\""
      elif app.Name == "输入法":
        progStr += "icon=\"" + image_dir_base + "/icons/" + icon_Theme + "/24x24/devices/input-keyboard.svg\""
      progStr += "><action name=\"Execute\"><command><![CDATA["
      if app.Terminal == True:
        progStr += terminal_string + " "
      progStr += "%s]]></command></action></item>"  % app.Exec
      print(progStr)
    print("</menu>")
  print("</openbox_pipe_menu>")    # magic footer
  pass # done/debug break
```

- jgmenu

```
# jgmenurc

stay_alive           = 1
tint2_look           = 0
position_mode        = fixed
terminal_exec        = termite
terminal_args        = -e
menu_width           = 200
menu_padding_top     = 40
menu_padding_right   = 2
menu_padding_bottom  = 5
menu_padding_left    = 2
menu_radius          = 0
menu_border          = 1
menu_halign          = left
sub_hover_action     = 1
item_margin_y        = 5
item_height          = 30
item_padding_x       = 8
item_radius          = 0
item_border          = 0
sep_height           = 5
font                 = Ubuntu 15px
icon_size            = 30
color_menu_bg        = #eeeeee 100
color_norm_bg        = #2b303b 0
color_norm_fg        = #000000 100
color_sel_bg         = #8fa1b3 60
color_sel_fg         = #2b303b 100
color_sep_fg         = #8fa1b3 40
```
```
# append.csv

^sep()
退出,^checkout(exit),system-shutdown
^tag(exit)
锁屏,slock,system-lock-screen
退出,openbox --exit,system-log-out
挂起,systemctl -i suspend,system-log-out
休眠,systemctl -i hibernate,system-hibernate
重启,systemctl -i reboot,system-reboot
关机,systemctl -i poweroff,system-shutdown
```
```
# prepend.csv

@rect,,5,10,190,30,2,left,top,#000000 0,#656565 50,
@search,,10,10,185,30,2,left,top,#eeeeee 80,#000000 0,
^sep()
终端,x-terminal-emulator,utilities-terminal
文件,thunar,system-file-manager
火狐,firefox-esr,firefox
^sep()
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
```
#---- Generated by tint2conf a94d ----
# See https://gitlab.com/o9000/tint2/wikis/Configure for 
# full documentation of the configuration options.
#-------------------------------------
# Gradients
#-------------------------------------
# Backgrounds
# Background 1: Panel
rounded = 0
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #eeeeee 100
border_color = #bbbbbb 100
background_color_hover = #eeeeee 100
border_color_hover = #bbbbbb 100
background_color_pressed = #eeeeee 100
border_color_pressed = #bbbbbb 100

# Background 2: Default task, Iconified task
rounded = 5
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #eeeeee 100
border_color = #eeeeee 100
background_color_hover = #eeeeee 100
border_color_hover = #cccccc 100
background_color_pressed = #cccccc 100
border_color_pressed = #cccccc 100

# Background 3: Active task
rounded = 5
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #dddddd 100
border_color = #999999 100
background_color_hover = #eeeeee 100
border_color_hover = #aaaaaa 100
background_color_pressed = #cccccc 100
border_color_pressed = #999999 100

# Background 4: Urgent task
rounded = 5
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #aa4400 100
border_color = #aa7733 100
background_color_hover = #aa4400 100
border_color_hover = #aa7733 100
background_color_pressed = #aa4400 100
border_color_pressed = #aa7733 100

# Background 5: Tooltip
rounded = 2
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #ffffaa 100
border_color = #999999 100
background_color_hover = #ffffaa 100
border_color_hover = #999999 100
background_color_pressed = #ffffaa 100
border_color_pressed = #999999 100

# Background 6: Inactive desktop name
rounded = 2
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #eeeeee 100
border_color = #cccccc 100
background_color_hover = #eeeeee 100
border_color_hover = #cccccc 100
background_color_pressed = #eeeeee 100
border_color_pressed = #cccccc 100

# Background 7: Active desktop name
rounded = 2
border_width = 1
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #dddddd 100
border_color = #999999 100
background_color_hover = #dddddd 100
border_color_hover = #999999 100
background_color_pressed = #dddddd 100
border_color_pressed = #999999 100

# Background 8: Systray
rounded = 3
border_width = 0
border_sides = TBLR
border_content_tint_weight = 0
background_content_tint_weight = 0
background_color = #dddddd 100
border_color = #cccccc 100
background_color_hover = #dddddd 100
border_color_hover = #cccccc 100
background_color_pressed = #dddddd 100
border_color_pressed = #cccccc 100

#-------------------------------------
# Panel
panel_items = LTEEEBSC
panel_size = 100% 40
panel_margin = 0 0
panel_padding = 4 2 4
panel_background_id = 1
wm_menu = 1
panel_dock = 0
panel_pivot_struts = 0
panel_position = bottom center horizontal
panel_layer = normal
panel_monitor = all
panel_shrink = 0
autohide = 0
autohide_show_timeout = 0
autohide_hide_timeout = 0.5
autohide_height = 2
strut_policy = follow_size
panel_window_name = tint2
disable_transparency = 0
mouse_effects = 1
font_shadow = 0
mouse_hover_icon_asb = 100 0 10
mouse_pressed_icon_asb = 100 0 0
scale_relative_to_dpi = 0
scale_relative_to_screen_height = 0

#-------------------------------------
# Taskbar
taskbar_mode = single_desktop
taskbar_hide_if_empty = 0
taskbar_padding = 0 0 2
taskbar_background_id = 0
taskbar_active_background_id = 0
taskbar_name = 0
taskbar_hide_inactive_tasks = 0
taskbar_hide_different_monitor = 0
taskbar_hide_different_desktop = 0
taskbar_always_show_all_desktop_tasks = 0
taskbar_name_padding = 6 3
taskbar_name_background_id = 6
taskbar_name_active_background_id = 7
taskbar_name_font = 霞鹜文楷 Bold 11
taskbar_name_font_color = #222222 100
taskbar_name_active_font_color = #222222 100
taskbar_distribute_size = 1
taskbar_sort_order = none
task_align = left

#-------------------------------------
# Task
task_text = 1
task_icon = 1
task_centered = 0
urgent_nb_of_blink = 100000
task_maximum_size = 140 35
task_padding = 4 3 4
task_font = 霞鹜文楷 10
task_tooltip = 1
task_thumbnail = 0
task_thumbnail_size = 210
task_font_color = #222222 100
task_icon_asb = 100 0 0
task_background_id = 2
task_active_background_id = 3
task_urgent_background_id = 4
task_iconified_background_id = 2
mouse_left = toggle_iconify
mouse_middle = none
mouse_right = close
mouse_scroll_up = prev_task
mouse_scroll_down = next_task

#-------------------------------------
# System tray (notification area)
systray_padding = 4 0 2
systray_background_id = 8
systray_sort = ascending
systray_icon_size = 22
systray_icon_asb = 100 0 0
systray_monitor = 1
systray_name_filter = 

#-------------------------------------
# Launcher
launcher_padding = 0 0 2
launcher_background_id = 0
launcher_icon_background_id = 0
launcher_icon_size = 38
launcher_icon_asb = 100 0 0
launcher_icon_theme = Papirus-Light
launcher_icon_theme_override = 0
startup_notifications = 1
launcher_tooltip = 1
launcher_item_app = /usr/share/applications/thunar.desktop
launcher_item_app = /usr/share/applications/sakura.desktop
launcher_item_app = /usr/share/applications/microsoft-edge.desktop
launcher_item_app = /usr/share/applications/sublime_text.desktop

#-------------------------------------
# Clock
time1_format = %F
time2_format = %H:%M
time1_font = 霞鹜文楷 Bold 10
time1_timezone = 
time2_timezone = 
time2_font = 霞鹜文楷 9
clock_font_color = #222222 100
clock_padding = 1 0
clock_background_id = 0
clock_tooltip = %A %F %H:%M 第%V周
clock_tooltip_timezone = 
clock_lclick_command = 
clock_rclick_command = 
clock_mclick_command = 
clock_uwheel_command = 
clock_dwheel_command = 

#-------------------------------------
# Battery
battery_tooltip = 1
battery_low_status = 10
battery_low_cmd = xmessage 'tint2: Battery low!'
battery_full_cmd = 
bat1_font = 霞鹜文楷 Bold 12
bat2_font = sans 6
battery_font_color = #222222 100
bat1_format = ⚡%p
bat2_format = 
battery_padding = 1 0
battery_background_id = 0
battery_hide = 101
battery_lclick_command = 
battery_rclick_command = 
battery_mclick_command = 
battery_uwheel_command = 
battery_dwheel_command = 
ac_connected_cmd = 
ac_disconnected_cmd = 

#-------------------------------------
# Executor 1
execp = new
execp_command = python3 /home/poo/.poo/network.py
execp_interval = 1
execp_has_icon = 0
execp_cache_icon = 1
execp_continuous = 0
execp_markup = 1
execp_monitor = all
execp_tooltip = 网络
execp_lclick_command = 
execp_rclick_command = 
execp_mclick_command = 
execp_uwheel_command = 
execp_dwheel_command = 
execp_font = 霞鹜文楷 Bold 12
execp_font_color = #000000 100
execp_padding = 0 0
execp_background_id = 0
execp_centered = 0
execp_icon_w = 0
execp_icon_h = 0

#-------------------------------------
# Executor 2
execp = new
execp_command = python3 /home/poo/.poo/volume.py
execp_interval = 1
execp_has_icon = 0
execp_cache_icon = 1
execp_continuous = 0
execp_markup = 1
execp_monitor = all
execp_tooltip = 声音
execp_lclick_command = 
execp_rclick_command = 
execp_mclick_command = 
execp_uwheel_command = 
execp_dwheel_command = 
execp_font = 霞鹜文楷 Bold 12
execp_font_color = #000000 100
execp_padding = 0 0
execp_background_id = 0
execp_centered = 0
execp_icon_w = 0
execp_icon_h = 0

#-------------------------------------
# Executor 3
execp = new
execp_command = echo "☀️$(light|cut --delimiter=. -f1)%"
execp_interval = 1
execp_has_icon = 0
execp_cache_icon = 1
execp_continuous = 0
execp_markup = 1
execp_monitor = all
execp_tooltip = 亮度
execp_lclick_command = 
execp_rclick_command = 
execp_mclick_command = 
execp_uwheel_command = 
execp_dwheel_command = 
execp_font = 霞鹜文楷 Bold 12
execp_font_color = #000000 100
execp_padding = 0 0
execp_background_id = 0
execp_centered = 0
execp_icon_w = 0
execp_icon_h = 0

#-------------------------------------
# Tooltip
tooltip_show_timeout = 0.5
tooltip_hide_timeout = 0.1
tooltip_padding = 2 2
tooltip_background_id = 5
tooltip_font_color = #222222 100
tooltip_font = 霞鹜文楷 11
```

### 14. 安装第三方软件

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

### 15. 缺少驱动

```
# 添加驱动
https://packages.debian.org/bookworm/firmware-misc-nonfree
```

### 16. 安装输入法

```
# sudo apt install ibus-rime librime-data-wubi
# /home/poo/.config/ibus/rime/default.custom.yaml
sudo apt install fcitx-rime librime-data-wubi
/home/poo/.config/fcitx/rime/default.custom.yaml
patch:
  "style/horizontal": true
  "menu/page_size": 5

  schema_list:
    - schema: wubi_pinyin
    - schema: luna_pinyin_simp
    - schema: wubi86
```
