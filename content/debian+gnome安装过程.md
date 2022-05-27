title: debian+gnome安装过程
date: 2021-04-08
category: debian
tag: gnome

[TOC]

### 1. 安装

### 2. 删除不需要软件

`apt autoremove --purge evolution libreoffice* gnome-calendar cheese gnome-chess gnome-clocks gnome-contacts evolution five-or-more four-in-a-row hitori gnome-klotski lightsoff gnome-mahjongg gnome-maps gnome-mines gnome-music gnome-nibbles quadrapassel gnome-robots gnome-sudoku swell-foop tali gnome-taquin gnome-tetravex gnome-todo totem gnome-2048 gnome-weather goldendict rhythmbox shotwell simple-scan synaptic termit transmission-gtk yelp zhcon aisleriot iagno gnome-sound-recorder fcitx5*`

### ibus-rime横排

1. 创建空白文件:
```
~/.config/ibus/rime/build/ibus_rime.yaml
```
2. 向 ibus_rime.yaml 写入并保存以下内容:
```
style:
   horizontal: true
```
3. 重新部署 ibus-rime