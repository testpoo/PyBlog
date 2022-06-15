	title: debian+kde安装过程
date: 2021-05-31
category: debian
tag: kde

[TOC]

### 1. 下载链接

<https://www.debian.org/download>

### 2. 下载驱动

<https://mirrors.tuna.tsinghua.edu.cn/debian-nonfree/firmware/bookworm/current/firmware.zip>

### 3. 制作自启动U盘

### 4. 安装

### 5. 去掉debain开机启动项停留的5秒和电池的问题

```
su root
nano /etc/sudoers添加 poo ALL=(ALL:ALL) ALL
nano /etc/default/grub
找到 GRUB_DEFAULT=x,并将x改为希望启动系统的序号,默认 x == 0，即默认启动项是 Debian,启动项从上往下数分别是 0 、 1 、 2 。。。
修改GRUB_TIMEOUT=5改为GRUB_TIMEOUT=0
修改GRUB_CMDLINE_LINUX_DEFAULT="quiet" 加acpi=force
sudo update-grub，该命令将刚才的修改更新至 /boot/grub/grub.cfg 文件中
```

### 6. 修改源

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

### 7. 安装软件

`sudo apt install intel-microcode fonts-noto-cjk arc-theme git fcitx-rime librime-data-wubi`

### 8. 删除不需要软件

`apt autoremove --purge kmail kaddressbook korganizer okular knotes akregator konqueror kwalletmanager k3b libreoffice*`

### 9. 安装图标主题

- 通过`https://github.com/yeyushengfan258/Win11-icon-theme`下载

- 进入`Win11-icon-theme`目录，执行`./install.sh -a`命令

### 10. 安装窗口装饰

- 通过`https://github.com/vinceliuice/Colloid-kde/`下载

- 安装窗口装饰元素`Colloid-light-round`到`~/.local/share/aurorae/themes/`下

### 11. 安装SDDM主题

- 通过`https://github.com/MarianArlt/kde-plasma-chili`下载

- 进入`kde-plasma-chili`目录，执行`cp -r kde-plasma-chili /usr/share/sddm/themes`命令

### 12. 解决无法更换头像

- 这是账号服务的一个缺陷: 打开`sudo nano /usr/lib/systemd/system/accounts-daemon.service`文件，修改`PrivateTmp=true`为`PrivateTmp=false`，然后重启即可解决问题。

### 13. 修改设置

- 桌面背景修改：设置-->更改壁纸-->壁纸类型：每日一图-->提供：必应

- 双击打开文件：设置-->点击文件或文件夹时-->选中他们

- 去掉程序特效：设置-->外观-->程序启动动效，沟选“无动效”，沟去“启动动效”。

- 去掉欢迎屏幕：设置-->外观-->欢迎屏幕选无。

- 锁屏背景修改：设置-->工作区行为-->锁屏-->配置-->壁纸类型：每日一图-->提供：必应

- 修改登录画面：设置-->开机与关机-->登录屏幕(SDDM)-->选择安装的新画面

- 修改用户头像：设置-->用户-->修改用户头像

- 触摸板设置：设置-->输入设备-->触摸板-->手指轻触

- 绽放设置：设置-->显示器配置-->全局缩放率：125%

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