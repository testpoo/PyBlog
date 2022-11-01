title: debian+kde设置
date: 2021-05-31
category: debian
tag: kde

[TOC]

### 1. 安装软件

`sudo apt install intel-microcode fonts-noto-cjk arc-theme git fcitx-rime librime-data-wubi`

### 2. 删除不需要软件

`apt autoremove --purge kmail kaddressbook korganizer okular knotes akregator konqueror kwalletmanager k3b libreoffice*`

### 3. 安装图标主题

- 通过`https://github.com/yeyushengfan258/Win11-icon-theme`下载

- 进入`Win11-icon-theme`目录，执行`./install.sh -a`命令

### 4. 安装窗口装饰

- 通过`https://github.com/vinceliuice/Colloid-kde/`下载

- 安装窗口装饰元素`Colloid-light-round`到`~/.local/share/aurorae/themes/`下

### 5. 安装SDDM主题

- 通过`https://github.com/MarianArlt/kde-plasma-chili`下载

- 进入`kde-plasma-chili`目录，执行`cp -r kde-plasma-chili /usr/share/sddm/themes`命令

### 6. 解决无法更换头像

- 这是账号服务的一个缺陷: 打开`sudo nano /usr/lib/systemd/system/accounts-daemon.service`文件，修改`PrivateTmp=true`为`PrivateTmp=false`，然后重启即可解决问题。

### 7. 修改设置

- 桌面背景修改：设置-->更改壁纸-->壁纸类型：每日一图-->提供：必应

- 双击打开文件：设置-->点击文件或文件夹时-->选中他们

- 去掉程序特效：设置-->外观-->程序启动动效，沟选“无动效”，沟去“启动动效”。

- 去掉欢迎屏幕：设置-->外观-->欢迎屏幕选无。

- 锁屏背景修改：设置-->工作区行为-->锁屏-->配置-->壁纸类型：每日一图-->提供：必应

- 修改登录画面：设置-->开机与关机-->登录屏幕(SDDM)-->选择安装的新画面

- 修改用户头像：设置-->用户-->修改用户头像

- 触摸板设置：设置-->输入设备-->触摸板-->手指轻触

- 绽放设置：设置-->显示器配置-->全局缩放率：125% 